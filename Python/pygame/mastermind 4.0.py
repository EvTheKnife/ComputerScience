import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
BOARD_X = WIDTH-40
BOARD_Y = HEIGHT//2
HINT_BOARD_X = BOARD_X
HINT_BOARD_Y = HEIGHT // 8
CENTER = (WIDTH/2, HEIGHT/2)


FPS = 60

RED = (200, 50, 50)
BLUE = (50, 50, 200)
YELLOW = (200, 200, 50)
GREEN = (50, 200, 50)
BLACK = (10, 10, 10)
WHITE = (240, 240, 240)

BG_COLOR = (50, 50, 100)
BOARD_COLOR = (40, 40, 40)
SPOT_COLOR = (75, 75, 75)



display = pygame.display.set_mode((WIDTH, HEIGHT))
FramePerSec = pygame.time.Clock()



run = True

while run:
    pygame.display.update()
    FramePerSec.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False