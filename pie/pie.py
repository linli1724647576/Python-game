import math
import pygame
import sys
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("送给寒武纪白")
myfont=pygame.font.SysFont('arial',30)

color=200,80,60
width=4
x=300
y=250
radius=200
position=x-radius,y-radius,radius*2,radius*2
white=255,255,255

piece1=False
piece2=False
piece3=False
piece4=False



while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
        elif event.type==KEYUP:
            if event.key==pygame.K_ESCAPE:
                sys.exit()
            elif event.key==pygame.K_1:
                piece1=True
            elif event.key==pygame.K_2:
                piece2=True
            elif event.key==pygame.K_3:
                piece3=True
            elif event.key==pygame.K_4:
                piece4=True

    #clear the screen
    screen.fill((0,0,200))

    #draw the four numbers
    textTmg1=myfont.render("1",True,color)
    screen.blit(textTmg1,(x+radius/2-20,y-radius/2))
    textTmg2=myfont.render("2",True,color)
    screen.blit(textTmg2,(x-radius/2,y-radius/2))
    textTmg3=myfont.render("3",True,color)
    screen.blit(textTmg3,(x-radius/2,y+radius/2-20))
    textTmg4=myfont.render("4",True,color)
    screen.blit(textTmg4,(x+radius/2-20,y+radius/2-20))
        
    #should the pieces be drawn?
    if piece1:
        start_angle=math.radians(0)
        end_angle=math.radians(90)
        pygame.draw.arc(screen,color,position,start_angle,end_angle,width)
        pygame.draw.line(screen,color,(x,y),(x,y-radius),width)
        pygame.draw.line(screen,color,(x,y),(x+radius,y),width)
    if piece2:
        start_angle=math.radians(90)
        end_angle=math.radians(180)
        pygame.draw.arc(screen,color,position,start_angle,end_angle,width)
        pygame.draw.line(screen,color,(x,y),(x,y-radius),width)
        pygame.draw.line(screen,color,(x,y),(x-radius,y),width)
    if piece3:
        start_angle=math.radians(180)
        end_angle=math.radians(270)
        pygame.draw.arc(screen,color,position,start_angle,end_angle,width)
        pygame.draw.line(screen,color,(x,y),(x-radius,y),width)
        pygame.draw.line(screen,color,(x,y),(x,y+radius),width)
    if piece4:
        start_angle=math.radians(270)
        end_angle=math.radians(360)
        pygame.draw.arc(screen,color,position,start_angle,end_angle,width)
        pygame.draw.line(screen,color,(x,y),(x,y+radius),width)
        pygame.draw.line(screen,color,(x,y),(x+radius,y),width)
    #is the pie finished?
    if piece1 and piece2 and piece3 and piece4:
        color=0,255,0
        textImage=myfont.render("You are beautiful",True,white)
        screen.blit(textImage,(180,230))
    pygame.display.update()
        
