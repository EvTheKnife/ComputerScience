import pygame
from pygame.locals import *


WIDTH = 800
HEIGHT = 600
FPS = 60

BG_COLOR = (250, 250, 230)
HOVER_COLOR = (200, 200, 200)
LINE_COLOR = (0, 0, 100)
O_COLOR = (250, 100, 100)
PLUS_COLOR = (100, 200, 100)

Turn = 0


pygame.init()

displaySurf = pygame.display.set_mode((WIDTH, HEIGHT))
FramePerSec = pygame.time.Clock()

class Lines(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, rgb):
        pygame.sprite.Sprite.__init__(self)

        self.surf = pygame.Surface((w, h))
        self.surf.fill(rgb)
        self.rect = self.surf.get_rect(center=(x,y))
        

class HitBox(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)

        self.surf = pygame.Surface((w, h))
        self.rect = self.surf.get_rect(topright=(x,y))

        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]


        if self.rect.collidepoint(mouse_x, mouse_y):
            self.surf.fill(HOVER_COLOR)
            if Turn == 0:
                pass
        if self.rect.collidepoint(mouse_x, mouse_y) == False:
            self.surf.fill(BG_COLOR)




displaySurf.fill(BG_COLOR)

BoardGroup = pygame.sprite.Group()

Vert_Line_1 = Lines(300, 300, 10, 500, LINE_COLOR)
Vert_Line_2 = Lines(500, 300, 10, 500, LINE_COLOR)
Horiz_Line_1 = Lines(400, 200, 500, 10, LINE_COLOR)
Horiz_Line_2 = Lines(400, 400, 500, 10, LINE_COLOR)


TLHitbox = HitBox(295, 50, 145, 145)


BoardGroup.add(Vert_Line_1, Vert_Line_2, Horiz_Line_1, Horiz_Line_2)



running = True

while running:

    for entity in BoardGroup:
        displaySurf.blit(entity.surf, entity.rect)

    displaySurf.blit(TLHitbox.surf, TLHitbox.rect)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    TLHitbox = HitBox(295, 50, 145, 145)


    pygame.display.update()
    FramePerSec.tick(FPS)