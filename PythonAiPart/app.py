from flask import Flask, jsonify, request
from flask_cors import CORS

from pathfinding import (
    bfs,
    dfs,
    astar,
    all_paths
)

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "message": "Python AI Server is Running!"
    })


@app.route("/ai_decision", methods=["POST"])
def ai_decision():

    data = request.json

    playerhp = data["playerhp"]
    bothp = data["bothp"]
    dist = data["dist"]

    hD = playerhp - bothp

    if hD >= 20:
        decision = "RETREAT"

    elif dist <= 1.8:
        decision = "MELEE_ATTACK"

    else:
        decision = "CHASE"

    return jsonify({
        "decision": decision,
        "playerhp": playerhp,
        "bothp": bothp,
        "dist": dist
    })


@app.route("/pathfind", methods=["POST"])
def pathfind():

    data = request.json

    botpos = tuple(
        data["botpos"]
    )

    playerpos = tuple(
        data["playerpos"]
    )

    obstacles = data.get(
        "obstacles",
        []
    )

    GRID = [
        [0 for x in range(30)]
        for y in range(16)
    ]

    for obstacle in obstacles:

        x = obstacle["x"]
        y = obstacle["y"]

        if (
            0 <= x < 30
            and 0 <= y < 16
        ):
            GRID[y][x] = 1

    bx, by = botpos
    px, py = playerpos

    if (
        0 <= bx < 30
        and 0 <= by < 16
    ):
        GRID[by][bx] = 0

    if (
        0 <= px < 30
        and 0 <= py < 16
    ):
        GRID[py][px] = 0

    paths = all_paths(
        GRID,
        botpos,
        playerpos
    )

    def convert_path(path):

        result = []

        for point in path:

            result.append({
                "x": point[0],
                "y": point[1]
            })

        return result

    aspath = convert_path(
        paths["astar"]
    )

    bfspath = convert_path(
        paths["bfs"]
    )

    dfspath = convert_path(
        paths["dfs"]
    )

    return jsonify({

        "botpos":
            list(botpos),

        "playerpos":
            list(playerpos),

        "aspath":
            aspath,

        "aslen":
            len(aspath),

        "bfspath":
            bfspath,

        "bfslen":
            len(bfspath),

        "dfspath":
            dfspath,

        "dfslen":
            len(dfspath)
    })


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000
    )