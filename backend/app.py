from flask import Flask, request, jsonify
import time
from typing_logic import calculate_result

app = Flask(__name__)

SENTENCE = "Typing speed improves with regular practice"

@app.route("/")
def home():
    return "Typing Speed Test Backend Running"

@app.route("/start", methods=["GET"])
def start():
    return jsonify({"sentence": SENTENCE, "start_time": time.time()})

@app.route("/result", methods=["POST"])
def result():
    data = request.json
    typed = data["typed"]
    start = data["start"]
    end = time.time()

    wpm, accuracy, time_taken = calculate_result(SENTENCE, typed, start, end)

    return jsonify({
        "wpm": wpm,
        "accuracy": accuracy,
        "time": time_taken
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
