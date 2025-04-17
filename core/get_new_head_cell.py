# /*===================================
#     Stock Imports
# ====================================*/

# ...

# /*===================================
#     Main
# ====================================*/

from common import globals as const

def get_new_head_cell(cells=const.SNAKE_CELLS):
    direction_to_use = const.DIRECTION_QUEUE[0]
    const.CURRENT_DIRECTION = direction_to_use

    # Remove the first item if there are queued directions (so the next one is used next tick)
    if len(const.DIRECTION_QUEUE) > 1:
        const.DIRECTION_QUEUE.pop(0)

    match const.CURRENT_DIRECTION:
        case "left":
            return cells[len(cells) - 1] - 1
        case "up":
            return cells[len(cells) - 1] - const.GRID_SIZE
        case "right":
            return cells[len(cells) - 1] + 1
        case "down":
            return cells[len(cells) - 1] + const.GRID_SIZE