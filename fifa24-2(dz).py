import pygame as pg
pg.init()

widht = 1000
height = 400
screen = pg.display.set_mode((widht, height))
pg.display.set_caption("Fifa23")
###################1 задание ############
color = (25,100,55)
while(1):
    for event in  pg.event.get():
        if event.type == pg.QUIT:
            exit()
    screen.fill(color)
    #################2 задание###################
    pg.draw.line(screen, (0,0,0), (1,0), (widht, height), 10) 
    pg.draw.polygon(screen, (255, 255,255), [(400, 100), (400, 50), (100, 150),])
    pg.draw.rect(screen, (193, 110, 24), (100, 150, 400, 100), 30, 10)


    ##############3 задание ##################
    pg.draw.rect(screen, (193, 10, 24), (600, 50, 300, 300), 0, 10)
    pg.draw.rect(screen, (193, 110, 24), (600, 50, 300, 300), 30, 10)

    pg.draw.circle(screen, (255,255,255), (50, 300), 30, )
    pg.draw.circle(screen, (0,0,0), (50, 300), 30, 5)
    
    pg.display.update()