# /*===================================
#     Stock Imports
# ====================================*/

import pygame

# /*===================================
#     Main
# ====================================*/

from common import globals as const

pygame.init()

pygame.display.set_caption("Snake Game")

GAME_WINDOW = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))

FONT_SMALL = pygame.font.SysFont("arial", 36)
FONT_LARGE = pygame.font.SysFont("arial", 72)