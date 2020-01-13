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
font2=pygame.font.SysFont('arial',28)
font3=pygame.font.SysFont('arial',200)
white=255,255,255
yellow=255,255,0

flag=0
screen.fill((0,100,0))
print_text(font1,0,160,"please press enter to begin")
print_text(font2,0,200," have a happy day")

#repeating loop
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
        elif event.type==KEYDOWN:
            key_flag=True
        elif event.type==KEYUP:
            key_flag=False
            if event.key==pygame.K_RETURN:
                flag=1
                #变量初始化
                key_flag=False
                game_over=False
                clock_start=time.time()
                seconds=21
                correct_answer=97
                speed=0
                score=0
    if flag:
        keys=pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()
        if keys[K_RETURN]:
            if  not game_over:
                game_over=False
                score=0
                seconds=21
                speed=0
                clock_start=time.time()
        if not game_over:
            current=time.time()-clock_start
            if seconds-current<0:
                game_over=True
            else:
                if keys[correct_answer]:
                    correct_answer=random.randint(97,122)
                    current=time.time()-clock_start
                    score+=1
                    speed=60*score/(current+0.1)

        #clear the screen
        screen.fill((0,100,0))
        print_text(font1,0,0,"Let's see how fast you can type!")
        print_text(font1,0,20,"Try to keep up for 10 seconds...")

        if key_flag:
            print_text(font1,500,0,"<key>")
        if not game_over:
            print_text(font1,0,80,"Time:"+str(int(seconds-current)))
        print_text(font1,0,100,"Speed:"+str(speed)+"letters/min")
        if game_over:
            print_text(font1,0,160,"You are beautiful")
            print_text(font1,0,180,"Please press enter to restart")
        print_text(font3,0,240,chr(correct_answer-32),yellow)
    

    pygame.display.update()
