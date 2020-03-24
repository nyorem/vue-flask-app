from flask import Flask, jsonify, make_response
from flask_cors import CORS
import time

app = Flask(__name__)
cors = CORS(app,
            resources={
                r"/api/*": { "origins": r"http://localhost:8080/*"},
            })

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({ "error": "Not found" }), 404)

@app.route("/api/time/")
def get_time():
    payload = {
        "time": time.time(),
    }

    return jsonify(payload)

if __name__ == "__main__":
    app.run(debug=True)
