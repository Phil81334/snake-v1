# /*===================================
#     Stock Imports
# ====================================*/

import sys

# /*===================================
#     Main
# ====================================*/

from common import globals as const
import singletons.pygame_ref as pygref

def show_game_over_screen():
    # Fill background
    background_color = (0, 0, 0)
    pygref.GAME_WINDOW.fill(background_color)

    # Render text
    text_game_over = pygref.FONT_LARGE.render("Game Over", True, (255, 0, 0))
    text_score = pygref.FONT_SMALL.render("Score: " + str(const.SCORE), True, (255, 255, 255))
    text_prompt = pygref.FONT_SMALL.render("Press any key to exit", True, (200, 200, 200))

    # Get rectangles to center text
    rect_game_over = text_game_over.get_rect(center=(pygref.GAME_WINDOW.get_width() // 2, pygref.GAME_WINDOW.get_height() // 2 - 60))
    rect_score = text_score.get_rect(center=(pygref.GAME_WINDOW.get_width() // 2, pygref.GAME_WINDOW.get_height() // 2))
    rect_prompt = text_prompt.get_rect(center=(pygref.GAME_WINDOW.get_width() // 2, pygref.GAME_WINDOW.get_height() // 2 + 60))

    # Draw text
    pygref.GAME_WINDOW.blit(text_game_over, rect_game_over)
    pygref.GAME_WINDOW.blit(text_score, rect_score)
    pygref.GAME_WINDOW.blit(text_prompt, rect_prompt)
    pygref.pygame.display.flip()

    # Wait for key press or quit
    waiting = True
    while waiting:
        for event in pygref.pygame.event.get():
            if event.type == pygref.pygame.QUIT:
                pygref.pygame.quit()
                sys.exit()
            if event.type == pygref.pygame.KEYDOWN:
                waiting = False
    
    pygref.pygame.quit()
    sys.exit()