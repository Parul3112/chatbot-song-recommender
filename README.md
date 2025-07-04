# Chatbot Song Recommender

This project is a chatbot-based song recommender system that suggests songs based on the user's mood and listening history.

## Features
- Chatbot interface to interact with users
- Mood detection from user messages using NLP
- Recommends songs based on mood and user history
- Uses a hybrid recommendation approach

## Technologies Used
- Python
- Flask
- Scikit-learn, NLTK
- SQLite
- HTML/CSS (basic frontend)

## How to Run

1. Clone or unzip this project.
2. Open terminal in the project directory.
3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the Flask server:
   ```
   python app.py
   ```
6. Open your browser and go to `http://127.0.0.1:5000/` to use the chatbot.

