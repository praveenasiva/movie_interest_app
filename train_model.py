import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load the data
csv_path = 'Movie_Interests.csv'
data = pd.read_csv(csv_path)

# Encode categorical target
interest_map = {label: idx for idx, label in enumerate(data['Interest'].unique())}
data['Interest_encoded'] = data['Interest'].map(interest_map)

# Features and target
X = data[['Age', 'Gender']]
y = data['Interest_encoded']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, 'model.pkl')

# Save mapping for later use
import json
with open('interest_map.json', 'w') as f:
    json.dump(interest_map, f)

print('Model and mapping saved successfully.')
