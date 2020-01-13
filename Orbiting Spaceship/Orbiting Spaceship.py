import sys,random,math,pygame
from pygame.locals import *

#Point class 
class Point(object):
    def __init__(self,x,y):
        self._x=x
        self._y=y

    #X property
    def getx(self):
        return self._x
    def setx(self,x):
        self._x=x
    x=property(getx,setx)

    #Y property
    def gety(self):
        return self._y
    def sety(self,y):
        self._y=y
    y=property(gety,sety)

#print_text function
def print_text(font,x,y,text,color=(255,255,255)):
    imgText=font.render(text,True,color)
    screen.blit(imgText,(x,y))

#wrap_angle function
def wrap_angle(angle):
    return angle%360

#main program begins
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("送给寒武纪白")
font=pygame.font.Font(None,18)

#load bitmaps
space=pygame.image.load("2.jpg").convert_alpha()
planet=pygame.image.load("3.jpg").convert_alpha()
ship=pygame.image.load("4.jpg").convert_alpha()
width,height=ship.get_size()
ship=pygame.transform.smoothscale(ship,(width//2,height//2))

radius=250
angle=0.0
pos=Point(0,0)
old_pos=Point(0,0)

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

    #draw planet
    width,height=planet.get_size()
    screen.blit(planet,(400-width/2,300-height/2))

    #move the ship
    angle=wrap_angle(angle-0.1)
    pos.x=math.sin(math.radians(angle))*radius
    pos.y=math.cos(math.radians(angle))*radius
    
    #rotate the ship
    delta_x=(pos.x-old_pos.x)
    delta_y=(pos.y-old_pos.y)
    rangle=math.atan2(delta_y,delta_x)
    rangled=wrap_angle(-math.degrees(rangle))
    scratch_ship=pygame.transform.rotate(ship,rangled)

    #draw the ship
    width,height=scratch_ship.get_size()
    x=400+pos.x-width//2
    y=300+pos.y-height//2
    screen.blit(scratch_ship,(x,y))

    print_text(font,0,0,"Orbit:"+"{:.0f}".format(angle))
    print_text(font,0,20,"Rotation:"+"{:.2f}".format(rangle))
    print_text(font,0,40,"Position:"+str(pos))
    print_text(font,0,60,"Old Pos:"+str(old_pos))

    pygame.display.update()
    #remember position
    old_pos.x=pos.x
    old_pos.y=pos.y