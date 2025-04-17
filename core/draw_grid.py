# /*===================================
#     Stock Imports
# ====================================*/

# ...

# /*===================================
#     Main
# ====================================*/

from common import globals as const
import singletons.pygame_ref as pygref

def draw_grid():
    # draw background
    pygref.GAME_WINDOW.fill(const.GRID_BACKGROUND_COLOR)

    # Draw vertical lines
    for x in range(const.GRID_SIZE):
        pygref.pygame.draw.line(
            pygref.GAME_WINDOW,
            const.GRID_LINE_COLOR,
            start_pos=(x * const.CELL_WIDTH, 0),
            end_pos=(x * const.CELL_WIDTH, pygref.GAME_WINDOW.get_height())
        )

    # Draw horizontal lines
    for y in range(const.GRID_SIZE):
        pygref.pygame.draw.line(
            pygref.GAME_WINDOW,
            const.GRID_LINE_COLOR,
            start_pos=(0, y * const.CELL_HEIGHT),
            end_pos=(pygref.GAME_WINDOW.get_width(), y * const.CELL_HEIGHT)
        )
    
    # Draw boundary cells
    for cell in const.EDGE_CELLS:
        row = cell // const.GRID_SIZE
        col = cell % const.GRID_SIZE
        rect = pygref.pygame.Rect(
            col * const.CELL_WIDTH,
            row * const.CELL_HEIGHT,
            const.CELL_WIDTH,
            const.CELL_HEIGHT
        )
        pygref.pygame.draw.rect(
            pygref.GAME_WINDOW,
            const.GRID_BOUNDARY_COLOR,
            rect
        )