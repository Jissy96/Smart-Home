from flask import Flask, request, jsonify
import os

app = Flask(__name__)

def announce(message):
    os.system(f"espeak '{message}'")  # Text-to-speech on Raspberry Pi

@app.route('/')
def home():
    return "Raspberry Pi Smart Home System is running!"

@app.route('/event', methods=['POST'])
def event():
    data = request.json
    event_type = data.get("event")

    responses = {
        "fire_alarm": "Fire alarm detected! Evacuate immediately.",
        "glass_breaking": "Possible intrusion detected! Alerting security.",
        "baby_crying": "Baby crying detected. Notifying guardian.",
        "doorbell": "Doorbell detected. Please check the entrance.",
        "gunshot": "Gunshot detected! Take cover and call emergency services.",
    }

    if event_type in responses:
        message = responses[event_type]
        announce(message)
        return jsonify({"message": message})

    return jsonify({"message": "Unknown event"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
