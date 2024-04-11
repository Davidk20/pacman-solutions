"""
File controlling the handling of the flask server and its routes.
"""
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from solving_pacman_backend.exceptions import LevelNotFoundException
from solving_pacman_backend.services import game_manager
from solving_pacman_backend.services import level_handler

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/")
def home():  # dead: disable
    """
    route for the root of the server.
    """
    return "<h1 style='color:blue'>Solving Pac-Man - Backend</h1>"


@app.route("/get-levels", methods=["GET"])
def get_levels():
    """Returns an overview of information about all levels."""
    return jsonify(level_handler.get_overview()), 200


@app.route("/get-game", methods=["GET"])
def get_board():
    """Route to return a game simulation."""
    level_num = int(request.args.get("level_num"))  # type: ignore
    try:
        game = game_manager.GameManager(
            level_num, configuration=game_manager.RunConfiguration.SERVER
        )
        message = game.game_loop()
        status = 200
    except LevelNotFoundException as e:
        message = str(e)
        status = 400
    return jsonify(message), status


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=4000)
