from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model and the interest mapping
model = joblib.load('model.pkl')
interest_map = joblib.load('interest_map.pkl')

# Make a new dictionary to change numbers back to interest names
interest_map_rev = {}
for interest, number in interest_map.items():
    interest_map_rev[number] = interest

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Get age and gender from the form
        age = int(request.form['age'])
        gender = int(request.form['gender'])
        # Use the model to predict the interest number
        pred_num = model.predict([[age, gender]])[0]
        # Get the interest name from the number
        prediction = interest_map_rev.get(pred_num, "Unknown")
    # Show the result on the web page
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)