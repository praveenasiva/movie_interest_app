# Movie Interest Prediction App
A simple web application that predicts a user's movie interest category (Animation, Action, or Drama) based on their age and gender, using a Decision Tree Classifier.

# Features
Predicts movie interests based on user input (age and gender)
Clean and intuitive web interface
Built using Python and Flask
Uses a Decision Tree Classifier for predictions

# Prerequisites
Make sure the following are installed:

Python 3.6 or higher
pip (Python package manager)

# Installation
1. Clone the repository
git clone https://github.com/yourusername/movie_interest_app.git
cd movie_interest_app
2. Install dependencies
pip install -r requirements.txt
3. Train the model (optional)
A pre-trained model (model.pkl) is already included. But if you want to retrain:
python train_model.py

# Running the Application
Start the Flask development server:
python app.py
Open your browser and go to:
http://localhost:5000

# How It Works
The app uses a Decision Tree Classifier trained on sample data from Movie_Interests.csv.
When a user submits their age and gender:
The model predicts a movie interest category.
The app then displays the predicted interest (Animation, Action, or Drama).

# File Structure
movie_interest_app/
├── app.py                # Flask application
├── train_model.py        # Script to train the ML model
├── model.pkl             # Pre-trained model
├── interest_map.pkl      # Mapping of interest categories
├── Movie_Interests.csv   # Sample training data
├── requirements.txt      # Python dependencies
├── render.yaml           # Deployment configuration
└── README.md             # Project documentation

# Future Improvements
Add more input features like location, favorite genre, etc.
Experiment with different machine learning models
Improve the UI using frontend frameworks

