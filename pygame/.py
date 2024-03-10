import pygame as pg

pg.init()

screen_width = 800
screen_height = 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Wooper")



running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    screen.fill((255, 255, 255))    
    image = pg.image.load("pygame\Woopa.png")
    image_rect = image.get_rect()
    image_rect.center = (screen_width // 2, screen_height // 2)
    screen.blit(image, image_rect)
    pg.display.flip() 

pg.quit()