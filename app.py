from flask import Flask, render_template, request
import joblib
import pandas as pd
import sys
import json

app = Flask(__name__)

# Load the model and mapping when the app starts
try:
    model = joblib.load('model.pkl')
    with open('interest_map.json', 'r') as f:
        interest_map = json.load(f)
    # Reverse the mapping for prediction
    interest_map_rev = {v: k for k, v in interest_map.items()}
except Exception as e:
    print(f"Error loading model or mapping: {e}", file=sys.stderr)
    model = None
    interest_map_rev = None

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            # Get form data
            age = int(request.form['age'])
            gender = int(request.form['gender'])
            if model and interest_map_rev:
                # Make prediction
                pred_num = model.predict([[age, gender]])[0]
                prediction = interest_map_rev.get(pred_num, "Unknown")
            else:
                prediction = "Model not loaded"
        except Exception as e:
            prediction = f"Invalid input: {e}"
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    print("Starting Flask app... Access it at http://127.0.0.1:5000/")
    app.run(debug=True)