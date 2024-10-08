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
clickedBoxes = []


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
    def __init__(self, x, y, w, h, boxPos):
        pygame.sprite.Sprite.__init__(self)

        self.surf = pygame.Surface((w, h))
        self.rect = self.surf.get_rect(topright=(x,y))


    def 
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        pressed1 = pygame.mouse.get_pressed()[0]


        if self.rect.collidepoint(mouse_x, mouse_y):
            self.surf.fill(HOVER_COLOR)
            if Turn == 0:
                pass
        if self.rect.collidepoint(mouse_x, mouse_y) == False:
            self.surf.fill(BG_COLOR)


        if self.rect.collidepoint(mouse_x, mouse_y) and pressed1:
            pass
            





displaySurf.fill(BG_COLOR)

BoardGroup = pygame.sprite.Group()
HitBoxesGroup = pygame.sprite.Group()

Vert_Line_1 = Lines(300, 300, 10, 500, LINE_COLOR)
Vert_Line_2 = Lines(500, 300, 10, 500, LINE_COLOR)
Horiz_Line_1 = Lines(400, 200, 500, 10, LINE_COLOR)
Horiz_Line_2 = Lines(400, 400, 500, 10, LINE_COLOR)

TLHitbox = HitBox(295, 50, 145, 145, 0)
MLHitbox = HitBox(295, 205, 145, 190, 3)
BLHitbox = HitBox(295, 405, 145, 145, 6)
TCHitbox = HitBox(495, 50, 190, 145, 1)
MCHitbox = HitBox(495, 205, 190, 190, 4)
BCHitbox = HitBox(495, 405, 190, 145, )
TRHitbox = HitBox(650, 50, 145, 145, 2)
MRHitbox = HitBox(650, 205, 145, 190, 5)
BRHitbox = HitBox(650, 405, 145, 145)





BoardGroup.add(Vert_Line_1, Vert_Line_2, Horiz_Line_1, Horiz_Line_2)



running = True

while running:

    for entity in BoardGroup:
        displaySurf.blit(entity.surf, entity.rect)
    
    
    displaySurf.blit(TLHitbox.surf, TLHitbox.rect)
    displaySurf.blit(TCHitbox.surf, TCHitbox.rect)
    displaySurf.blit(MLHitbox.surf, MLHitbox.rect)
    displaySurf.blit(MCHitbox.surf, MCHitbox.rect)
    displaySurf.blit(BLHitbox.surf, BLHitbox.rect)
    displaySurf.blit(BCHitbox.surf, BCHitbox.rect)
    displaySurf.blit(TRHitbox.surf, TRHitbox.rect)
    displaySurf.blit(MRHitbox.surf, MRHitbox.rect)
    displaySurf.blit(BRHitbox.surf, BRHitbox.rect)




    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False







    pygame.display.update()
    FramePerSec.tick(FPS)