from flask import Flask

app = Flask(__name__)

@app.route("/orders")
def orders():
    return "<h1>Order service running!</h1>"

# New route to show HTML image
@app.route("/orders/image")
def orders_with_image():
    return """
    <h1>Order Service Image</h1>
    <img src='https://via.placeholder.com/300' alt='Order Image'>
    """

app.run(host="0.0.0.0", port=5002)
