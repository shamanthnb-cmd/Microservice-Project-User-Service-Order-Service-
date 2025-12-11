from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/orders")
def users():
    return jsonify({"message": "order service running!"})

app.run(host="0.0.0.0", port=5001)
