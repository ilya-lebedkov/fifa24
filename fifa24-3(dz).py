import pygame as pg
pg.init()

widht = 800
height = 800
screen = pg.display.set_mode((widht, height))
pg.display.set_caption("fifyshka")

x = 100
y = 100
x3 = 100
y3 = 100

x2 = 700
y2 = 100
step = 0.5
step2 = 0.5
step3 = 0.5
step4 = 0.5

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    screen.fill((153,23,213))
    ###############1задание#############
    x3 += step3
    if x3 > 550:
        step3 = -step3
    if x3 < 0:
        step3 = -step3
    
    y3 += step4
    if y3 > 800:
        step4 = -step4
    if y3 < 0:
        step4 = -step4

    
    pg.draw.rect(screen, (13,123,223), (x3, 300, 300, 200), )
    pg.draw.circle(screen, (234,234,234), (100, y3), 100)

    
    x += step
    if x > 700:
        step = -step
    if x < 0:
        step = -step
    
    y += step2
    if y > 700:
        step2 = -step2
    if y < 0:
        step2 = -step2  

    y2 += step2
    x2 -= step2
        

    pg.draw.circle(screen, (255, 0, 0), (x, y), 100)
    pg.draw.circle(screen, (0,0,255), (x2, y2), 100)
    
    pg.display.update()