import pygame
from pygame.locals import *
import random
import time



WIDTH = 800
HEIGHT = 600
FPS = 20
frame = 0

SKY_COLOR = (0, 0, 0)
STAR_COLOR = (255, 255, 255)
FADE_COLORS = [(200, 200, 200), (150, 150, 150), (100, 100, 100), (50, 50, 50), (25, 25, 25)]

displaySurf = pygame.display.set_mode((WIDTH, HEIGHT))
FramePerSec = pygame.time.Clock()



star_X = random.randint(30, 770)
star_Y = random.randint(30, 570)


displaySurf.fill(SKY_COLOR)

pygame.draw.circle(displaySurf, STAR_COLOR, (star_X, star_Y), 10)


running = True

while running:

    

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    
    if frame % 20 == 0 or frame % 20 == 1:
        displaySurf.fill(SKY_COLOR)

    else:
        star_X = random.randint(30, 770)
        star_Y = random.randint(30, 570)
        pygame.draw.circle(displaySurf, STAR_COLOR, (star_X, star_Y), 10)
        for i in range (5):
            pygame.draw.circle(displaySurf, FADE_COLORS[i], (star_X, star_Y), 10)
            time.sleep(0.1)


    


    frame += 1

    pygame.display.update()
    FramePerSec.tick(FPS)