from flask import Flask, jsonify, request
from flask_cors import CORS
from data import Event,events

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message":"Welcome to events manager"}),200

@app.route("/events",methods = ['GET'])
def get_events():
    all_events = [event.to_dict() for event in events]
    if all_events:
        return jsonify(all_events),200
    else:
        return f"No events to show at the moment",404

@app.route("/events",methods=["POST"])
def add_event():
    data = request.get_json()
    if 'title' in data:
        id = max([event.id for event in events],default=0) + 1
        new_event = Event(id,data["title"])
        events.append(new_event)
        return jsonify(new_event.to_dict()),201
    else:
        return "Please provide a valid event title",400
if __name__ == "__main__":
    app.run(debug=True)
