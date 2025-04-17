# /*===================================
#     Stock Imports
# ====================================*/

import random

# /*===================================
#     Main
# ====================================*/

from common import globals as const
from core.add_direction_to_queue import add_direction_to_queue
from core.close_event import close_event
from core.draw_cell import draw_cell
from core.draw_grid import draw_grid
from core.draw_score import draw_score
from core.get_new_head_cell import get_new_head_cell
from core.show_game_over_screen import show_game_over_screen
import singletons.pygame_ref as pygref

# LET'S GOOOOO!
def update_snake_cells_list():
    # get said cell b4 anything else
    const.CURRENT_CELL = const.SNAKE_CELLS[len(const.SNAKE_CELLS) -1]

    # add new head cell based on current direction
    new_cell = get_new_head_cell()

    if new_cell in const.SNAKE_CELLS:
        show_game_over_screen()

    # grow: no tail removal
    if new_cell == const.FOOD_CELL:
        const.SNAKE_CELLS.append(new_cell)
        const.SCORE += 10

        # spawn new food
        while True:
            new_food_cell = random.choice(random.choice(const.GRID))
            if new_food_cell not in const.EDGE_CELLS \
                and new_food_cell not in const.SNAKE_CELLS \
                and new_food_cell != const.FOOD_CELL:
                const.FOOD_CELL = new_food_cell
                break
    else:
        const.SNAKE_CELLS.pop(0)           # remove tail
        const.SNAKE_CELLS.append(new_cell) # move forward
    
    # detect if new cell is edge cell or the snake itself
    if new_cell in const.EDGE_CELLS:
        show_game_over_screen()
    
    const.LAST_SNAKE_UPDATE_TIME = pygref.pygame.time.get_ticks()

def draw_snake():
    for cell in const.SNAKE_CELLS:
        draw_cell(cell, const.SNAKE_COLOR)

def draw_food():
    draw_cell(const.FOOD_CELL, const.FOOD_COLOR)

# event loop
while True:
    # handle events
    for event in pygref.pygame.event.get():
        if event.type == pygref.pygame.QUIT:
            close_event(event)
        if event.type == pygref.pygame.KEYDOWN:
            # handle user input
            add_direction_to_queue(event)
    
    draw_grid()
    draw_snake()
    draw_food()
    draw_score()

    # update cells in the SNAKE_CELLS list
    if pygref.pygame.time.get_ticks() - const.LAST_SNAKE_UPDATE_TIME >= const.SNAKE_SPEED:
        update_snake_cells_list()
    
    # update display
    pygref.pygame.display.update()

    # add delay
    pygref.pygame.time.delay(const.GAME_EVENT_LOOP_SPEED)
