from flask import Flask

app = Flask(__name__)

@app.route("/users")
def users():
    return "<h1>User service running!</h1>"

# New route to show HTML image
@app.route("/users/image")
def users_with_image():
    return """
    <h1>User Service Image</h1>
    <img src='https://via.placeholder.com/300' alt='User Image'>
    """

app.run(host="0.0.0.0", port=5001)
