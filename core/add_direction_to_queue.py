# /*===================================
#     Stock Imports
# ====================================*/

# ...

# /*===================================
#     Main
# ====================================*/

from common import globals as const
import singletons.pygame_ref as pygref

def add_direction_to_queue(event):
    # print(f"Event: {event}")
    if event.type == pygref.pygame.KEYDOWN:
        # print(f"Key Pressed: {event.key}")
        if event.key == pygref.pygame.K_LEFT:
            const.DIRECTION_QUEUE.append("left")
        elif event.key == pygref.pygame.K_UP:
            const.DIRECTION_QUEUE.append("up")
        elif event.key == pygref.pygame.K_DOWN:
            const.DIRECTION_QUEUE.append("down")
        elif event.key == pygref.pygame.K_RIGHT:
            const.DIRECTION_QUEUE.append("right")

    # print(f"Direction Queue: {const.DIRECTION_QUEUE}")