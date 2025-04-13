import pygame as pg   
pg.init()

widht, height = 800, 600
screen = pg.display.set_mode((widht, height))

x = 0
y = 300

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((255,255,255))

    x += 1
    if x  > 800:
        x = -200
    

    pg.draw.rect(screen, (123,123,123),(x,y,200,100),0,20)
    pg.display.update()