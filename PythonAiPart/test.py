import requests


# AI Decision Test
data = {
    "player_health": 50,
    "bot_health": 60,
    "distance": 2
}

response = requests.post(
    "http://127.0.0.1:5000/ai_decision",
    json=data
)

print(response.json())


# Dynamic Pathfinding Test
print("\n--- Dynamic Pathfinding Test ---")

path_data = {
    "bot_position": [0, 0],
    "player_position": [6, 6],
    "algorithm": "astar"
}

response = requests.post(
    "http://127.0.0.1:5000/pathfind",
    json=path_data
)

print(response.json())