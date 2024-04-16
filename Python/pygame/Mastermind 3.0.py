import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

red = (200, 50, 50)
blue = (50, 50, 200)
yellow = (200, 200, 50)
green = (50, 200, 50)
black = (10, 10, 10)
white = (240, 240, 240)

bg_color = (100, 100, 200)


display = pygame.display.set_mode((WIDTH, HEIGHT))
FramePerSec = pygame.time.Clock()



font = pygame.font.Font("freesansbold.ttf", 32)

text = font.render('yes', True, black)
textRect = text.get_rect(center = (WIDTH/2, HEIGHT/4))
textRect.center = (WIDTH/2, HEIGHT/4)

running = True
while running:

    display.fill(bg_color)

    display.blit(text, textRect)


    pygame.display.update()
    FramePerSec.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False