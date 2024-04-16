import pygame
import random

pygame.init()

WIDTH=800
HEIGHT=600
FPS=20
frame = 0

SKY_COLOR = (0, 0, 0)
STAR_COLOR = (255, 255, 255)
star_color_fade = [255, 255, 255]


displaySurf = pygame.display.set_mode((WIDTH, HEIGHT))
framePerSec = pygame.time.Clock()

star_x=random.randint(30, 770)
star_y=random.randint(30, 570)
star_rad=random.randint(4, 10)

displaySurf.fill(SKY_COLOR)


pygame.draw.circle(displaySurf, STAR_COLOR, (star_x, star_y), star_rad)

running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                running=False


    if frame % 20 == 0:
        pygame.draw.circle(displaySurf, SKY_COLOR, (star_x, star_y), star_rad)
        star_color_fade[0] = 255
        star_color_fade[1] = 255
        star_color_fade[2] = 255
        star_x=random.randint(30, 770)
        star_y=random.randint(30, 570)
        star_rad=random.randint(4, 10)
        pygame.draw.circle(displaySurf, STAR_COLOR, (star_x, star_y), star_rad)
    else:
        star_color_fade[0] = star_color_fade[0] * .8
        star_color_fade[1] = star_color_fade[1] * .8
        star_color_fade[2] = star_color_fade[2] * .8
        pygame.draw.circle(displaySurf, star_color_fade, (star_x, star_y), star_rad)
   
    frame += 1

   
    pygame.display.update()
    framePerSec.tick(FPS)

