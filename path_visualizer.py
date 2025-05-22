import pygame
import sys
from euclidean_astar import a_star

# Initialize Pygame
pygame.init()

# Grid settings
GRID_SIZE = 50  # Number of cells
CELL_SIZE = 15  # Pixels per cell
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
start = (0, 0)
goal = (GRID_SIZE - 1, GRID_SIZE - 1)
path = []

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up window
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("A* Pathfinding Demo")

# Main loop
running = True
setting_start = False
setting_goal = False
setting_obstacles = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                setting_start = True
                setting_goal = False
                setting_obstacles = False
            elif event.key == pygame.K_g:
                setting_goal = True
                setting_start = False
                setting_obstacles = False
            elif event.key == pygame.K_o:
                setting_obstacles = True
                setting_start = False
                setting_goal = False
            elif event.key == pygame.K_SPACE:
                path = a_star(grid, start, goal)  # Run A*
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row, col = pos[1] // CELL_SIZE, pos[0] // CELL_SIZE
            if setting_start:
                start = (row, col)
            elif setting_goal:
                goal = (row, col)
            elif setting_obstacles:
                grid[row][col] = 1 if grid[row][col] == 0 else 0

    # Draw grid
    screen.fill(WHITE)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            color = WHITE if grid[row][col] == 0 else BLACK
            if (row, col) == start:
                color = GREEN
            elif (row, col) == goal:
                color = RED
            elif (row, col) in path:
                color = BLUE
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, (200, 200, 200), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    pygame.display.flip()

pygame.quit()
sys.exit()
