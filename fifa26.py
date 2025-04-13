import pygame as pg   
pg.init()

widht, height = 1000, 800
screen = pg.display.set_mode((widht, height))

x = 0
y = 300
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

    key = pg.key.get_pressed()
    if key[pg.K_s]:
        y += step

    key = pg.key.get_pressed()
    if key[pg.K_a]:
        x -= step
    
    key = pg.key.get_pressed()
    if key[pg.K_d]:
        x += step

    if key[pg.K_LSHIFT]:
        step = 3
    else: 
        step = 1

    if key[pg.K_r]:
        step = 300000000


    if key[pg.K_f] and key[pg.K_r]:
        x = 650
        y = 150
        print('откуда инфа?')

    if x < 0:
        x = 0
    if x > 800:
        x = 800
    if y < 0:
        y = 0
    if y > 700:
        y = 700
    
    
    
    pg.draw.rect(screen, (255,255,0),(600,40,300,300),0,200)
    pg.draw.rect(screen, (0,0,0),(600,40,300,300),10,200)
    pg.draw.rect(screen, (243,5,40),(x,y,200,100),0,20)
    pg.draw.rect(screen, (23,50,40),(x,y,100,100),10,20)
    pg.display.update()