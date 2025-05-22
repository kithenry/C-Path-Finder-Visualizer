import heapq

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = [(0, start)]  # Priority queue: (f_score, node)
    came_from = {}  # Parent map for path reconstruction
    g_score = {start: 0}  # Cost from start to node
    f_score = {start: abs(goal[0] - start[0]) + abs(goal[1] - start[1])}  # f = g + h (Manhattan)

    closed = set()  # Visited nodes

    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Reverse path

        closed.add(current)

        # Check neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                if neighbor in closed:
                    continue
                tentative_g_score = g_score[current] + 1  # Cost to neighbor

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + abs(goal[0] - neighbor[0]) + abs(goal[1] - neighbor[1])
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return []  # No path found

# Example usage
grid = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (4, 4)
path = a_star(grid, start, goal)
print("Path:", path)
