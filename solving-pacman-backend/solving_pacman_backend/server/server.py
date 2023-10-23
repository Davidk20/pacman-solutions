"""
File controlling the handling of the flask server and its routes.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():  # dead: disable
    """
    route for the root of the server.
    """
    return "<h1 style='color:blue'>Hello There!</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=1000)
