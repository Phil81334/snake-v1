# /*===================================
#     Stock Imports
# ====================================*/

import sys

# /*===================================
#     Main
# ====================================*/

import singletons.pygame_ref as pygref

def close_event(event):
    if event.type == pygref.pygame.QUIT:
        print("Close button clicked.")
        pygref.pygame.quit()
        sys.exit()