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






def hintBoard():
    hintBoard.surf = pygame.Surface((HINT_BOARD_X, HINT_BOARD_Y))
    hintBoard.surf.fill(BOARD_COLOR)
    hintBoard.rect = hintBoard.surf.get_rect(center =(CENTER[0], CENTER[1] - (HEIGHT // 3)))

inputPinSpotList = []
hintPinSpotList = []
hintDividerLineList = []

def Board():
    Board.surf = pygame.Surface((BOARD_X, BOARD_Y))
    Board.surf.fill(BOARD_COLOR)
    Board.rect = Board.surf.get_rect(center = CENTER)

    for x in range (12):
        for y in range(4):
            inputPinSpot = pygame.Rect(((x*BOARD_X//12) + BOARD_X//12) - 30, ((y*BOARD_Y//4) + BOARD_X//4) - 15, 30, 30)
            inputPinSpotList.append(inputPinSpot)

    for x in range (24):
        for y in range (2):
            hintPinSpot = pygame.Rect((x * HINT_BOARD_X//24) + BOARD_X//24, (y*HINT_BOARD_Y//2) + HINT_BOARD_Y, 10, 10)
            hintPinSpotList.append(hintPinSpot)
    
    for x in range(11):
        dividerLine = pygame.Rect(((x*BOARD_X//12) + BOARD_X//12) + 20, CENTER[1]//4-12, 3, HINT_BOARD_Y)
        hintDividerLineList.append(dividerLine)

def pins():
    for i in range(len(inputPinSpotList)):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if inputPinSpotList[i].collidepoint(pygame.mouse.get_pos()) and event.key == pygame.K_1 :
                    pygame.draw.rect(display, RED, inputPinSpotList[i])


Board()
hintBoard()





running = True
while running:

    display.fill(BG_COLOR)


    display.blit(Board.surf, Board.rect)
    display.blit(hintBoard.surf, hintBoard.rect)
                
    for inputPinSpot in inputPinSpotList:
        for hintPinSpot in hintPinSpotList:
            pygame.draw.rect(display, SPOT_COLOR, inputPinSpot)
            pygame.draw.rect(display, SPOT_COLOR, hintPinSpot)
    for dividerLine in hintDividerLineList:
        pygame.draw.rect(display, BLACK, dividerLine) 

    pins()
    pygame.display.update()
    FramePerSec.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False