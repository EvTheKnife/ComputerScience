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

turn = 0

display = pygame.display.set_mode((WIDTH, HEIGHT))
FramePerSec = pygame.time.Clock()

input_spots = pygame.sprite.Group()

class input_spots(pygame.sprite.Sprite):
    def __init__(self, size, center_pos):
        pygame.sprite.Sprite.__init__(self)
        
        self.surf = pygame.Surface(size)
        color = 0
        self.rect = self.surf.get_rect(center = center_pos)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if self.rect.collidepoint(pygame.mouse.get_pos()) and event.key == pygame.K_1 :
                    color = 1
                    print("yes")
                if self.rect.collidepoint(pygame.mouse.get_pos()) and event.key == pygame.K_2 :
                    color = 2
                if self.rect.collidepoint(pygame.mouse.get_pos()) and event.key == pygame.K_3 :
                    color = 3
                if self.rect.collidepoint(pygame.mouse.get_pos()) and event.key == pygame.K_4 :
                    color = 4
                if self.rect.collidepoint(pygame.mouse.get_pos()) and event.key == pygame.K_5 :
                    color = 5
                if self.rect.collidepoint(pygame.mouse.get_pos()) and event.key == pygame.K_6 :
                    color = 6

                 
        if color == 0:
            self.surf.fill(SPOT_COLOR)
        if color == 1:
            self.surf.fill(RED)
        if color == 2:
            self.surf.fill(BLUE)
                 
                 
                 
                 
                 
def main_board():
    main_board.surf = pygame.Surface((BOARD_X, BOARD_Y))
    main_board.surf.fill(BOARD_COLOR)
    main_board.rect = main_board.surf.get_rect(center = CENTER)

def hint_board():
    hint_board.surf = pygame.Surface((HINT_BOARD_X, HINT_BOARD_Y))
    hint_board.surf.fill(BOARD_COLOR)
    hint_board.rect = hint_board.surf.get_rect(center =(CENTER[0], CENTER[1] - (HEIGHT // 3)))



spot_1 = input_spots((20, 20), (300, 300))

display.fill(BG_COLOR)
main_board()
hint_board()


run = True

while run:

    display.blit(hint_board.surf, hint_board.rect)
    display.blit(main_board.surf, main_board.rect)

    display.blit(spot_1.surf, spot_1.rect)


    pygame.display.update()
    FramePerSec.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False