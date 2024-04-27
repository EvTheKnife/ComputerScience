import pygame
import random

pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT= 500
Font=pygame.font.SysFont('timesnewroman',  20)
def draw_text(text,font,col,x,y):
    img=font.render(text,True,col)
    screen.blit(img,(x,y))

screen= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
cells=[]
for x in range(10):
    for y in range(10):
        cell=pygame.Rect(x * 50,y * 50,40,40)
        cells.append(cell)
Dificulty= 15
badcells= []
for num in range(Dificulty):
    x=random.randint(0,9)
    y=random.randint(0,9)
    badcells.append((x,y))
print(badcells)

zerocells = []
clickedcells=[]
suscells=[]
Notclicked= (100,100,100)
clicked= (255,255,255)
run= True

winscreen=pygame.Rect(0,0,500,500)

while run:
    screen.fill((0,0,0))
    pos = pygame.mouse.get_pos()
    for cell in cells:
        clickness = Notclicked
        if pygame.mouse.get_pressed()[0] and cell.collidepoint(pos):
            if (cell.x /50 , cell.y /50) in badcells:
                run= False
            elif cell.collidepoint(pos) and cell not in clickedcells:
                clickedcells.append(cell)
            if cell in suscells:
                suscells.remove(cell)
        elif pygame.mouse.get_pressed()[2] and cell.collidepoint(pos) and (cell not in suscells):
            suscells.append(cell)
        else:
            pygame.draw.rect(screen,clickness, cell)

    for cell in clickedcells:
        pygame.draw.rect(screen, clicked, cell)
        closecount=0
        for x in range(-1,2):
            for y in range(-1,2):
                if ((cell.x /50 )+ x, (cell.y /50 )+y) in badcells:
                    closecount = closecount+1
        if closecount== 0:
            for x in range(-1, 2):
                for y in range(-1, 2):
                    for allcell in cells:
                        if ((allcell.x == cell.x + (x*50)) and (allcell.y == cell.y + (y*50))) and (allcell not in clickedcells) and (allcell not in badcells):
                            clickedcells.append(allcell)

        draw_text(str(closecount), Font, (255, 0, 0), cell.x + 20, cell.y + 20)

    for cell in zerocells:
        pygame.draw.rect(screen, clicked, cell)

    for cell in suscells:
        pygame.draw.rect(screen, (255,0,0), cell)

    if len(clickedcells) == (100-Dificulty):
        pygame.draw.rect(screen, (0,255,0), winscreen)
        draw_text("YOU WIN!!!", Font, (255, 0, 0), 150, 250)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()

