# /*===================================
#     Stock Imports
# ====================================*/

import random

# /*===================================
#     Main
# ====================================*/

# ...

# milliseconds
GAME_EVENT_LOOP_SPEED = 16  # ~60 fps

# milliseconds
SNAKE_SPEED = 250

# milliseconds
# we dont want snake moving at same speed as event loop,
# so we check if curr time - last update time >= snake speed,
# to ensure snake moves at consistent speed thats separated from event loop
LAST_SNAKE_UPDATE_TIME = 0

# track direction
# upon game start, snake moves toward right-edge of screen
CURRENT_DIRECTION = "right"

# screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# grid dimensions
GRID_SIZE = 20  # stick to intervals of 20
CELL_WIDTH = SCREEN_WIDTH // GRID_SIZE
CELL_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# colors
GRID_BACKGROUND_COLOR = (0, 0, 0)
GRID_LINE_COLOR = (125, 125, 125)
GRID_BOUNDARY_COLOR = (128, 0, 32)

SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (245, 222, 179)

# grid cells
# check out ../docs/grid-visualization.md
GRID = []
current = 0
for i in range(GRID_SIZE):
    row = []
    for j in range(GRID_SIZE):
        row.append(current)
        current += 1
    GRID.append(row)
# print grid
# print("[")
# for row in GRID:
#     print(f"    {row},")
# print("]")

INITIAL_SNAKE_LENGTH = 5

# list of cells that snake is currently occupying
SNAKE_CELLS = []
row_index = GRID_SIZE // 2
col_start = (GRID_SIZE // 2) - (INITIAL_SNAKE_LENGTH // 2)
for j in range(col_start, col_start + INITIAL_SNAKE_LENGTH):
    SNAKE_CELLS.append(GRID[row_index][j])
print(f"SNAKE_CELLS: {SNAKE_CELLS}")

# list of cells that are on the edge of the grid
EDGE_CELLS = []
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        is_top = i == 0
        is_bottom = i == GRID_SIZE - 1
        is_left = j == 0
        is_right = j == GRID_SIZE - 1

        if is_top or is_bottom or is_left or is_right:
            EDGE_CELLS.append(GRID[i][j])
# print(f"EDGE_CELLS: {EDGE_CELLS}")

FOOD_CELL = None
while True:
    new_food_cell = random.choice(random.choice(GRID))
    if new_food_cell not in EDGE_CELLS:
        FOOD_CELL = new_food_cell
        break
print(f"FOOD_CELL: {FOOD_CELL}")

CURRENT_CELL = None

SCORE = 0

DIRECTION_QUEUE = [CURRENT_DIRECTION]