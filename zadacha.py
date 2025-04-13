import pygame as pg   
pg.init()

widht, height = 500, 500
screen = pg.display.set_mode((widht, height))

x = 150
y = 150
step = 1

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            

    screen.fill((155,255,255))
    
    key = pg.key.get_pressed()
    if key[pg.K_w]:
        y -= step
    if event.type == pg.KEYUP:
        x = 150
        y = 150

    key = pg.key.get_pressed()
    if key[pg.K_s]:
        y += step
    
    if event.type == pg.KEYUP:
        x = 150
        y = 150

    key = pg.key.get_pressed()
    if key[pg.K_a]:
        x -= step
    if event.type == pg.KEYUP:
        x = 150
        y = 150
    
    key = pg.key.get_pressed()
    if key[pg.K_d]:
        x += step
    if event.type == pg.KEYUP:
        x = 150
        y = 150
    


    if x < 0:
        x = 0
    if x > 400:
        x = 400
    if y < 0:
        y = 0
    if y > 400:
        y = 400

    pg.draw.rect(screen, (23,50,40),(x,y,100,100),0,2110)
    pg.display.update()