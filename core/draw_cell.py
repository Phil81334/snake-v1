# /*===================================
#     Stock Imports
# ====================================*/

# ...

# /*===================================
#     Main
# ====================================*/

from common import globals as const
import singletons.pygame_ref as pygref

def draw_cell(cell, color):
    pygref.pygame.draw.rect(
        pygref.GAME_WINDOW,
        color,
        rect=(
            cell % const.GRID_SIZE * const.CELL_WIDTH, 
            cell // const.GRID_SIZE * const.CELL_HEIGHT, 
            const.CELL_WIDTH, 
            const.CELL_HEIGHT
        )
    )
