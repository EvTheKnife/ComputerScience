from typing import Any
import pygame
from pygame.locals import *
import random

pygame.init()

vec = pygame.math.Vector2

HIGHT = 200
WIDTH = 800
ACC = 0.5
FRIC = -0.12
FPS = 60

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption("Game")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.surf = pygame.image.load('images/Woopa.png')
        self.surf = pygame.transform.scale(self.surf, (100, 100))
        self.rect = self.surf.get_rect()
        

        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def move(self):
        self.acc = vec(0,0.5)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
            self.surf = pygame.image.load('images/Woopa_Flipped.png')
            self.surf = pygame.transform.scale(self.surf, (100, 100))

        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
            self.surf = pygame.image.load('images/Woopa.png')
            self.surf = pygame.transform.scale(self.surf, (100, 100))

        
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.acc.y += self.vel.y * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        self.rect.midbottom = self.pos

        if self.pos.y > HIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HIGHT
    
    def update(self):
        hits = pygame.sprite.spritecollide(P1, platforms, False)
        if P1.vel.y > 0:
            if hits:
                self.pos.y = hits[0].rect.top + 1
                self.vel.y = 0

    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.vel.y = -15

class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50, 100), 12))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center = ((random.randint(0, WIDTH-10), random.randint(0, HIGHT-30))))




PT1 = platform()
PT1.surf = pygame.Surface((WIDTH, 20))
PT1.surf.fill((255,255,255))
PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HIGHT - 10))


P1 = Player()

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(PT1)
platforms.add(PT1)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    displaysurface.fill((0, 0, 0))
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
    for entity in platforms:
        displaysurface.blit(entity.surf, entity.rect)
    
    
    P1.move()
    P1.update()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            P1.jump()


    pygame.display.update()
    FramePerSec.tick(FPS)