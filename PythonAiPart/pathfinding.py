from collections import deque
import heapq


def get_neighbors(grid, node):
    rows = len(grid)
    cols = len(grid[0])

    x, y = node

    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    neighbors = []

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if (
            0 <= nx < cols
            and 0 <= ny < rows
            and grid[ny][nx] == 0
        ):
            neighbors.append((nx, ny))

    return neighbors


def reconstruct_path(parent, start, goal):
    if goal not in parent and goal != start:
        return []

    path = []
    current = goal

    while current != start:
        path.append(current)
        current = parent[current]

    path.append(start)
    path.reverse()

    return path


def bfs(grid, start, goal):

    queue = deque([start])
    visited = {start}
    parent = {}

    while queue:

        current = queue.popleft()

        if current == goal:
            return reconstruct_path(
                parent,
                start,
                goal
            )

        for neighbor in get_neighbors(grid, current):

            if neighbor not in visited:

                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return []


def dfs(grid, start, goal):

    stack = [start]
    visited = {start}
    parent = {}

    while stack:

        current = stack.pop()

        if current == goal:
            return reconstruct_path(
                parent,
                start,
                goal
            )

        for neighbor in get_neighbors(grid, current):

            if neighbor not in visited:

                visited.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)

    return []


def heuristic(a, b):

    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):

    open_set = []

    heapq.heappush(
        open_set,
        (0, start)
    )

    parent = {}

    g_score = {
        start: 0
    }

    while open_set:

        _, current = heapq.heappop(
            open_set
        )

        if current == goal:

            return reconstruct_path(
                parent,
                start,
                goal
            )

        for neighbor in get_neighbors(
            grid,
            current
        ):

            tentative_g = (
                g_score[current] + 1
            )

            if (
                neighbor not in g_score
                or tentative_g < g_score[neighbor]
            ):

                parent[neighbor] = current

                g_score[neighbor] = tentative_g

                f_score = (
                    tentative_g +
                    heuristic(
                        neighbor,
                        goal
                    )
                )

                heapq.heappush(
                    open_set,
                    (f_score, neighbor)
                )

    return []


def all_paths(grid, start, goal):

    return {
        "astar": astar(
            grid,
            start,
            goal
        ),

        "bfs": bfs(
            grid,
            start,
            goal
        ),

        "dfs": dfs(
            grid,
            start,
            goal
        )
    }