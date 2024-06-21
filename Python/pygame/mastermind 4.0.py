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

input_spots = pygame.sprite.Group()

class input_spots(pygame.sprite.Sprite):
    def __init__(self, size, center_pos, color):
        pygame.sprite.Sprite.__init__(self)
        
        self.surf = pygame.Surface(size)
        self.surf.fill(color)
        self.rect = self.surf.get_rect(center = center_pos)

rect1 = input_spots((20, 20), (300, 300), RED)

input_spots.add(rect1)


def hintBoard():
    hintBoard.surf = pygame.Surface((HINT_BOARD_X, HINT_BOARD_Y))
    hintBoard.surf.fill(BOARD_COLOR)
    hintBoard.rect = hintBoard.surf.get_rect(center =(CENTER[0], CENTER[1] - (HEIGHT // 3)))



display.fill(BG_COLOR)
hintBoard()

run = True

while run:

    display.blit(hintBoard.surf, hintBoard.rect)

    #for entity in input_spots:
    
        display.blit(entity.surf, entity.rect)

    pygame.display.update()
    FramePerSec.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False