from flask import Flask, session, request, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "supersecretkey123"  # Required for sessions to work
CORS(app)  # Allow requests from other origins (like React)

@app.route('/sessions/<string:key>', methods=['GET'])
def show_session(key):
    # Set some default session values if they don't exist
    session["hello"] = session.get("hello") or "World"
    session["goodnight"] = session.get("goodnight") or "Moon"

    # Build response including cookies and session info
    response = make_response(jsonify({
        "session": {
            "session_key": key,
            "session_value": session[key],
            "session_accessed": session.accessed,
        },
        "cookies": [{cookie: request.cookies[cookie]} for cookie in request.cookies],
    }), 200)

    # Set a regular cookie
    response.set_cookie("mouse", "Cookie")

    return response

@app.route('/')
def index():
    return "Go to /sessions/hello to see session and cookies in action!"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
