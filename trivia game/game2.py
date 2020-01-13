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
        '''f=open(filename,"r")
        trivia_data=f.readlines()   #trivia_data是一个列表
        f.close()'''

        #临时改的
        
        trivia_data=['The ship Titanic had been given the extra name of "unsinkable" because its ____ was the best there was.',\
        'manufacture',\
        'production',\
        'erection',\
        'construction',\
        '4',\
        'The US dollar is traditionally the ____ of choice all over the world in case of crisis.',\
        'money',\
        'currency',\
        'bill',\
        'cash',\
        '2',\
        'The education provides them ____ to economic progress.',\
        'admission',\
        'acceptance',\
        'approach',\
        'access',\
        '4',\
        'Japan has ____ its steps toward putting into effect an international treaty banning chemical weapons.',\
        'hurried',\
        'bustled',\
        'accelerated',\
        'rushed',\
        '3',\
        'The motion of ocean water ____ at different depths below the surface.',\
        'varies',\
        'modifies',\
        'alters',\
        'differs',\
        '1',\
        'Health experts ____ leisurely meals.',\
        'introduce',\
        'recommend',\
        'present',\
        'comment',\
        '2',\
        'Developing countries should adopt labour-intensive technologies to ____ their comparative advantage of abundant labour.',\
        'use',\
        'exploit',\
        'employ',\
        'explore',\
        '2',\
        'The sudden demise of Britain s oldest investment bank ____ global markets.',\
        'vibrated',\
        'swung',\
        'trembled',\
        'jolted',\
        '4',\
        'The tests show the earlier in life a person hears a sound the longer it is ____.',\
        'retained',\
        'preserved',\
        'remained',\
        'reserved',\
        '1',\
        'The researchers test college students ____ to foreign speech before their second birthday but not since.',\
        'disclosed',\
        'exposed',\
        'exhibited',\
        'revealed',\
        '2',\
        'The government has provided the capital library with heavy ____ to keep it one of the largest in the world.',\
        'subscriptions',\
        'tips',\
        'subsidies',\
        'bonuses',\
        '3',\
        'The doctor took his temperature, it was two degrees above ____.',\
        'ordinary',\
        'average',\
        'regular',\
        'normal',\
        '4']

        #count and clean up trivia data   每一行都是列表中的一项
        for text_line in trivia_data:
            self.data.append(text_line.strip())  #去掉末尾的换行符
            self.total+=1
        print(self.data)
    def show_question(self):
        if(self.end==0):
            print_text(font1,410,5,"ENGLISH TEST")
            print_text(font2,380,500-20,"Press Keys (1-4) To Start Again",purple)
            print_text(font2,410,500-55,"Press Keys (5) To Answer",purple)
            print_text(font2,730,5,"SCORE",purple)
            print_text(font2,750,25,str(self.score),purple)

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
                print_text(font1,600-170,380-20,"CORRECT!",green)
                print_text(font2,600-220,420-20,"Press Enter For Next Question",green)
            elif self.failed:
                self.colors=[white,white,white,white]
                self.colors[self.wronganswer-1]=red
                self.colors[self.correct-1]=green
                print_text(font1,600-170,380-20,"INCORRECT",red)
                print_text(font2,600-220,420-20,"Press Enter For Next Question",red)

            #display answers
            print_text(font1,5,170,"ANSWERS")
            print_text(font2,20,210,"1-"+self.data[self.current+1],self.colors[0])
            print_text(font2,20,240,"2-"+self.data[self.current+2],self.colors[1])
            print_text(font2,20,270,"3-"+self.data[self.current+3],self.colors[2])
            print_text(font2,20,300,"4-"+self.data[self.current+4],self.colors[3])
        elif(self.end==1):
            if(self.score>=10):
                print_text(font1,600-50,380,"EXCELLENT",red)
            elif(8<=self.score<=10):
                print_text(font1,600-50,380,"GOOD",red)
            elif(self.score<8):
                print_text(font1,600-50,380,"BAD",red)
            print_text(font2,600-70,200,"Thank You",red)
            print_text(font2,600-100,250,"You are beautiful",red)
    def handle_input(self,number):
        if not self.scored and not self.failed:
            if number==self.correct:
                self.scored=True
                self.score+=1
            else:
                self.failed=True
                self.wronganswer=number

    def start_again(self):
        if self.scored or self.failed:
            self.scored=False
            self.failed=False
            self.correct=0  #正确答案
            self.colors=[white,white,white,white]
            self.current=0
            self.score=0
            self.wronganswer=0
        
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
screen=pygame.display.set_mode((1200,550))                    
pygame.display.set_caption("送给寒武纪白升级版")
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
trivia=Trivia("English language test.txt")

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
            elif event.key==pygame.K_5:
                trivia.start_again()

    #clear the screen
    screen.fill((0,0,200))

    #display trivia data
    trivia.show_question()

    #updata.display
    pygame.display.update()

