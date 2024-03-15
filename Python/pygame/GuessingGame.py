import pygame
from pygame.locals import *
import pygame_menu
import pygame_gui


pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))


running = True

while running:

    menu = pygame_menu.menu.Menu("Guess", WIDTH/3, HEIGHT/3)

    menu.add.text_input('Why me: ')


    menu.mainloop(screen)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False