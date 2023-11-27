"""
File controlling the handling of the flask server and its routes.
"""
from flask import Flask
from flask import jsonify
from flask import request
from solving_pacman_backend.services.level_handler import LevelHandler
from solving_pacman_backend.services.level_handler import (
    LevelNotFoundException,
)

app = Flask(__name__)


# TODO - Once there is enough data, create useful root page.
@app.route("/")
def home():  # dead: disable
    """
    route for the root of the server.
    """
    return "<h1 style='color:blue'>Solving Pac-Man - Backend</h1>"


@app.route("/get-levels", methods=["GET"])
def get_levels():
    """Returns an overview of information about all levels."""
    level_handler = LevelHandler()
    return jsonify(level_handler.get_overview()), 200


@app.route("/get-board", methods=["GET"])
def get_board():
    """Route to return a game board."""
    level_num = int(request.args.get("level_num"))
    level_handler = LevelHandler()
    try:
        message = level_handler.get_level(level_num)
        status = 200
    except LevelNotFoundException as e:
        message = str(e)
        status = 400
    finally:
        level_handler.close()
    return jsonify(message), status


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=1000)
