# /*===================================
#     Stock Imports
# ====================================*/

# ...

# /*===================================
#     Main
# ====================================*/

from common import globals as const
import singletons.pygame_ref as pygref

def draw_score():
    score_text = pygref.FONT_SMALL.render("Score: " + str(const.SCORE), True, (255, 255, 255))
    # Draw in top left corner, with some padding
    pygref.pygame.display.get_surface().blit(score_text, (10, 10))