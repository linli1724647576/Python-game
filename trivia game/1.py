import sys
import pygame
from pygame.locals import *

class Trivia(object):
    def __init__(self,filename):
        self.data=[]    #数据列表用于存放数据
        self.current=0   
        self.total=0    
        self.correct=0  
        self.score=0        #所得分数
        self.scored=False   #答题正确
        self.failed=False   #答题错误
        self.wronganswer=0
        self.end=0
        self.colors=[white,white,white,white]   #颜色列表

        #read trivia data from file
        f=open(filename,"r")
        trivia_data=f.readlines()   #trivia_data是一个列表
        f.close()

        #count and clean up trivia data   每一行都是列表中的一项
        for text_line in trivia_data:
            self.data.append(text_line.strip())  #去掉末尾的换行符
            self.total+=1
        print(self.data)
    def show_question(self):
        if(self.end==0):
            print_text(font1,210,5,"TRIVIA GAME")
            print_text(font2,190,500-20,"Press Keys (1-4) To Answer",purple)
            print_text(font2,530,5,"SCORE",purple)
            print_text(font2,550,25,str(self.score),purple)

            #get correct answer out of data(first)
            self.correct=int(self.data[self.current+5])

            #display question
            question=self.current//6+1
            print_text(font1,5,80,"QUESTION"+str(question))
            print_text(font2,20,120,self.data[self.current],yellow)

            #respond to correct answer
            if self.scored:
                self.colors=[white,white,white,white]
                self.colors[self.correct-1]=green
                print_text(font1,230,380,"CORRECT!",green)
                print_text(font2,170,420,"Press Enter For Next Question",green)
            elif self.failed:
                self.colors=[white,white,white,white]
                self.colors[self.wronganswer-1]=red
                self.colors[self.correct-1]=green
                print_text(font1,220,380,"INCORRECT",red)
                print_text(font2,180,420,"Press Enter For Next Question",red)

            #display answers
            print_text(font1,5,170,"ANSWERS")
            print_text(font2,20,210,"1-"+self.data[self.current+1],self.colors[0])
            print_text(font2,20,240,"2-"+self.data[self.current+2],self.colors[1])
            print_text(font2,20,270,"3-"+self.data[self.current+3],self.colors[2])
            print_text(font2,20,300,"4-"+self.data[self.current+4],self.colors[3])
        elif(self.end==1):
            if(self.score>=5):
                print_text(font1,280,380,"EXCELLENT",red)
            elif(3<=self.score<=4):
                print_text(font1,280,380,"GOOD",red)
            elif(self.score<3):
                print_text(font1,280,380,"BAD",red)
            print_text(font2,270,200,"Thank You",red)
    def handle_input(self,number):
        if not self.scored and not self.failed:
            if number==self.correct:
                self.scored=True
                self.score+=1
            else:
                self.failed=True
                self.wronganswer=number
        
    def next_question(self):
        if self.scored or self.failed:
            self.scored=False
            self.failed=False
            self.correct=0  #正确答案
            self.colors=[white,white,white,white]
            self.current+=6
            if self.current>=self.total:  #结束标志
                self.current=0
                self.end=1

#主代码
def print_text(font,x,y,text,color=(255,255,255),shadow=True):
    if shadow:
        imgText=font.render(text,True,(0,0,0))
        screen.blit(imgText,(x-2,y-2))
    imgText=font.render(text,True,color)
    screen.blit(imgText,(x,y))

#main program begins
pygame.init()
screen=pygame.display.set_mode((650,550))                    
pygame.display.set_caption("The Trivia Game")
font1=pygame.font.SysFont('arial',40)                 
font2=pygame.font.SysFont('arial',24)
font3=pygame.font.SysFont('arial',60)
white=255,255,255
cyan=0,255,255
yellow=255,255,0
purple=255,0,255
green=0,255,0
red=255,0,0
End=0
#load the trivia data file
trivia=Trivia("trivia_data.txt")

#repeating loop
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
        elif event.type==KEYUP:
            if event.key==pygame.K_ESCAPE:
                sys.exit()
            elif event.key==pygame.K_1:
                trivia.handle_input(1)
            elif event.key==pygame.K_2:
                trivia.handle_input(2)
            elif event.key==pygame.K_3:
                trivia.handle_input(3)
            elif event.key==pygame.K_4:
                trivia.handle_input(4)
            elif event.key==pygame.K_RETURN:
                trivia.next_question()

    #clear the screen
    screen.fill((0,0,200))

    #display trivia data
    trivia.show_question()

    #updata.display
    pygame.display.update()


