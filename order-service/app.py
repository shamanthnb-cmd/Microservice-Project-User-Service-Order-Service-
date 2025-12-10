from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/users")
def users():
    return jsonify({"message": "User service running!"})

app.run(host="0.0.0.0", port=5001)
