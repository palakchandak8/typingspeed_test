from flask import Flask, request, jsonify, send_from_directory
import time, os
from backend.typing_logic import calculate_result

app = Flask(__name__, static_folder='frontend')

SENTENCE = "Typing speed improves with regular practice"

@app.route("/")
def home():
    return send_from_directory('frontend', 'index.html')

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory('frontend', filename)

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
    return jsonify({"wpm": wpm, "accuracy": accuracy, "time": time_taken})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

### Step 3: Add a `startup.txt` or configure startup command in Azure

Go to **Azure Portal → typingspeedtest → Configuration → General Settings → Startup Command** and enter:
```
gunicorn --bind=0.0.0.0:8000 app:app
