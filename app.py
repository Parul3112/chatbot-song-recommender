from flask import Flask, render_template, request
from utils.mood_detection import detect_mood
from utils.recommender import recommend_song

app = Flask(__name__)

user_history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    user_input = request.form["msg"]
    mood = detect_mood(user_input)
    recommended = recommend_song(mood, user_history)
    user_history.append(recommended)
    return {"response": recommended, "mood": mood}

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)
