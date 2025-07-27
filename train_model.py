import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# 1. Load the data from CSV file
data = pd.read_csv('Movie_Interests.csv')

# 2. Give each unique interest a number
interest_names = data['Interest'].unique()  # Get all unique interests
interest_map = {}  # Create an empty dictionary
for i in range(len(interest_names)):
    interest_map[interest_names[i]] = i  # Assign a number to each interest

# 3. Replace interest names with numbers in the data
data['Interest_encoded'] = data['Interest'].map(interest_map)

# 4. Select features (inputs) and target (output)
X = data[['Age', 'Gender']]  # Features: Age and Gender
y = data['Interest_encoded']  # Target: Encoded Interest

# 5. Train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# 6. Save the trained model and the mapping
joblib.dump(model, 'model.pkl')
joblib.dump(interest_map, 'interest_map.pkl')

print('Model and mapping saved successfully.')
