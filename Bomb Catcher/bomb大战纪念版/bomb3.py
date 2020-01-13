#Bomb Catcher Game
import sys,random,time,pygame
from pygame.locals import *

def print_text(font,x,y,text,color=(255,255,255)):
    imgText=font.render(text,True,color)
    screen.blit(imgText,(x,y))

#main program begins
pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("送给寒武纪白")
font1=pygame.font.SysFont('arial',24)
pygame.mouse.set_visible(False)
white=255,255,255
red=220,50,50
yellow=230,230,50
black=0,0,0

#绘制位图背景
img0=pygame.image
space=pygame.image.load("resources/hanwuji.jpg").convert()

#选择难度变量
color=200,80,60
white=255,255,255
piece1=False
piece2=False
piece3=False
piece4=False

screen.fill((0,0,150))
screen.blit(space,(0,0))
myfont=pygame.font.SysFont('arial',30)
myfont2=pygame.font.SysFont('arial',50)
print_text(myfont2,150,30,"BOMB GAME",yellow)
print_text(myfont,200,90,"enjoy you time",yellow)
print_text(font1,15,320,"press keys(1-4) to choose the level")
print_text(font1,15,360,"move your mouse to catch the bomb")


#repeating loop
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
        elif event.type==KEYUP:
            if event.key==pygame.K_ESCAPE:
                sys.exit()
            elif event.key==pygame.K_1:
                vel_y=0.5
                piece1=True
            elif event.key==pygame.K_2:
                vel_y=0.7
                piece2=True
            elif event.key==pygame.K_3:
                vel_y=0.9
                piece3=True
            elif event.key==pygame.K_4:
                vel_y=1.1
                piece4=True
    if piece1 or piece2 or piece3 or piece4:
        break
    pygame.display.update()
if piece1 or piece2 or piece3 or piece4:
    #初始化
    lives=3
    score=0
    game_over=True
    mouse_x=mouse_y=0
    pos_x=300
    pos_y=460
    bomb_x=random.randint(0,500)
    bomb_y=-50
    
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                sys.exit()
            elif event.type==MOUSEMOTION:
                mouse_x,mouse_y=event.pos
                move_x,move_y=event.rel
            elif event.type==MOUSEBUTTONUP:
                if game_over:
                    game_over=False
                    lives=3
                    score=0
    

        keys=pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()

        screen.fill((0,0,100))
        screen.blit(space,(0,0))

        if game_over:
            print_text(font1,100,300,"<CLICK TO PLAY>")
            print_text(font1,100,340,"SCORE:"+str(score))
            print_text(font1,100,380,"You are beautiful")
        else:
            #move the bomb
            bomb_y+=vel_y

            #has the player missed the bomb?
            if bomb_y>500:
                bomb_x=random.randint(0,500)
                bomb_y=-50
                lives-=1
                if lives==0:
                    game_over=True

            #see if player has caught the bomb
            elif bomb_y>pos_y:
                if bomb_x>pos_x and bomb_x<pos_x+120:
                    score+=10
                    bomb_x=random.randint(0,500)
                    bomb_y=-50

            #draw the bomb
            pygame.draw.circle(screen,black,(bomb_x-4,int(bomb_y)-4),30,0)
            pygame.draw.circle(screen,yellow,(bomb_x,int(bomb_y)),30,0)

            #set basket position
            pos_x=mouse_x
            if pos_x<0:
                pos_x=0
            elif pos_x>500:
                pos_x=500

            #draw basket
            pygame.draw.rect(screen,black,(pos_x-4,pos_y-4,120,40),0)
            pygame.draw.rect(screen,red,(pos_x,pos_y,120,40),0)

            #print # of lives
            print_text(font1,0,0,"LIVES:"+str(lives))

            #print score
            print_text(font1,460,0,"SCORE:"+str(score))
    
        pygame.display.update()
