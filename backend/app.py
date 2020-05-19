from flask import Flask, jsonify, make_response
from flask_cors import CORS
import time

app = Flask(__name__, static_folder="../frontend/dist", static_url_path="/")
cors = CORS(app,
            resources={
                r"/api/*": { "origins": [ "http://localhost:8080", "http://127.0.0.1:8080", # if using two dev servers (backend at 5000 and frontend at 808)
                                          "http://localhost:5000", "http://127.0.0.1:5000" ] # if using one dev server for the backend at 5000 and built files for the frontend
                            },
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

# we serve the index file at the root path (need 'npm run build' to be run in 'frontend' folder before)
@app.route("/")
def index():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
