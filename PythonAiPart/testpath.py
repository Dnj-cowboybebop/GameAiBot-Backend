from pathfinding import GRID, bfs, dfs, a_star


bot_position = (0, 0)
player_position = (6, 6)


# BFS
path = bfs(GRID, bot_position, player_position)

print("BFS Shortest Path:")
print(path)

print("BFS Path Length:", len(path))


# DFS
print("\nDFS Path:")

dfs_path = dfs(GRID, bot_position, player_position)

print(dfs_path)

print("DFS Path Length:", len(dfs_path))

# A*
print("\nA* Path:")

astar_path = a_star(
    GRID,
    bot_position,
    player_position
)

print(astar_path)

print("A* Path Length:", len(astar_path))