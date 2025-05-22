import heapq
import math

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = [(0, start)]  # Priority queue: (f_score, node)
    came_from = {}  # Parent map for path reconstruction
    g_score = {start: 0}  # Cost from start to node
    # Use Euclidean distance for heuristic (better for diagonal movement)
    f_score = {start: math.sqrt((goal[0] - start[0])**2 + (goal[1] - start[1])**2)}

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

        # Check neighbors (8 directions: up, down, left, right, and diagonals)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                if neighbor in closed:
                    continue
                # Cost: 1 for cardinal directions, sqrt(2) for diagonals
                cost = 1 if dx == 0 or dy == 0 else math.sqrt(2)
                tentative_g_score = g_score[current] + cost

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    # Use Euclidean distance for heuristic
                    h_score = math.sqrt((goal[0] - neighbor[0])**2 + (goal[1] - neighbor[1])**2)
                    f_score[neighbor] = g_score[neighbor] + h_score
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return []  # No path found
