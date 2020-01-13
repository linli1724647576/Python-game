import sys,random,math,pygame
from pygame.locals import *

#main program begins
pygame.init()
screen=pygame.display.set_mode((400,300))
pygame.display.set_caption("Orbit Demo")

#load bitmaps
space=pygame.image.load("D:\\python游戏\\Orbiting Spaceship\\potw1843a.jpg").convert()

#repeating loop
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
    keys=pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    #draw background
    screen.blit(space,(0,0))

    pygame.display.update()
