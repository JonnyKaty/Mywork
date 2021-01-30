#print("Hello, world!")
#print('Hello, world!')
##a line to divide
#def draw_box():
#    print("+-------+")
#    print("|       |")
#    print("|       |")
#    print("+-------+")
#draw_box()
#draw_box()
#print(1+1)
##pow
#print(2**2)
##int / int 
#print(9//2) 
#for i in range(5):
#    print("I am handsome.")
##printing a complex pic
#for line in range(1,6):
#    print("#" * line, end="")
#    print("+" * (2 * line), end="")
#    print("#" * line)
#for line in range(1,6):
#    print(" " * (line -1 ),end="")
#    print("*" * (11- 2 * line))
#for line in range(5,0,-1):
#    print(" " * (line -1 ),end="")
#    print("*" * (11- 2 * line))
##Prints a solid line of dashes.
#def draw_line():
#    print("+",end="")
#    print("-" * 10,end="")
#    print("+")

##参数过多，可拆分代码块
##my_fuction_call(a,b * c - 19,\
##d * f)
#x = 3.647;
#print("nearest integer is", round(x))
#print("nearest tenth is", round(x,1))
#print("nearest hundredth is", round(x,2))
#print("x is",x)
#import math
#import random
#import time

##def main():
##    STEPS = 20
##    position = 10

##    for i in range(STEPS):
##        time.sleep(0.2)
##        rnd = random.randrange(-1,2,2)
##        position += rnd
##        print(" " * position,"*")

##main()

##print((126.4 / 2) / (1.75 * 1.75))
##name = input("What's your name?")
##print("Hello",name) 

#from DrawingPanel import *
#panel = DrawingPanel(400,300)
##panel.background = "red"
#panel.draw_image("circles.png",0,0)
#panel.color = "green"
#panel.draw_oval(25,50,20,20)
#panel.fill_rect(150,10,40,20)

#s = "hello"
#try:
#    n = int(s)
#    print("I converted it successfully!",n)
#except ValueError:
#    #pass
#    print("s is a non-integer value.")

#print()


#import turtle
#def koch(size, n):
#    if n == 0:
#        turtle.fd(size)
#    else:
#        for angle in [0, 60, -120, 60]:
#           turtle.left(angle)
#           koch(size/3, n-1)
#def main():
#    turtle.setup(600,600)
#    turtle.penup()
#    turtle.goto(-200, 100)
#    turtle.pendown()
#    turtle.pensize(2)
#    level = 1      # 3阶科赫雪花，阶数
#    koch(400,level)     
#    turtle.right(120)
#    koch(400,level)
#    turtle.right(120)
#    koch(400,level)
#    turtle.hideturtle()
#main()


#import turtle, time
#def drawGap(): #绘制数码管间隔
#    turtle.penup()
#    turtle.fd(5)
#def drawLine(draw):   #绘制单段数码管
#    drawGap()
#    turtle.pendown() if draw else turtle.penup()
#    turtle.fd(40)
#    drawGap()
#    turtle.right(90)
#def drawDigit(d): #根据数字绘制七段数码管
#    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
#    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
#    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
#    drawLine(True) if d in [0,2,6,8] else drawLine(False)
#    turtle.left(90)
#    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
#    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
#    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
#    turtle.left(180)
#    turtle.penup()
#    turtle.fd(20)
#def drawDate(date):
#    turtle.pencolor("red")
#    for i in date:
#        if i == '-':
#            turtle.write('年',font=("Arial", 18, "normal"))
#            turtle.pencolor("green")
#            turtle.fd(40)
#        elif i == '=':
#            turtle.write('月',font=("Arial", 18, "normal"))
#            turtle.pencolor("blue")
#            turtle.fd(40)
#        elif i == '+':
#            turtle.write('日',font=("Arial", 18, "normal"))
#        else:
#            drawDigit(eval(i))
#def main():
#    turtle.setup(800, 350, 200, 200)
#    turtle.penup()
#    turtle.fd(-350)
#    turtle.pensize(5)
##    drawDate('2018-10=10+')
#    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
#    turtle.hideturtle()
#    turtle.done()
#main()

import requests
#r = requests.get("http://www.baidu.com")
#print(r.status_code)
#r.text


#爬虫通用模板
def get_status(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'} 
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'

#url = "https://www.amazon.cn/dp/B0040GJL0U/ref=s9_acsd_al_\
#bw_c2_x_0_i?pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised\
#-search-8&pf_rd_r=VAZGFRKQYDP1ZMAA3FKD&pf_rd_t=101&pf_rd\
#_p=ee9063e3-1862-4b40-a457-8074025f9723&pf_rd_i=888474051"
#url = "http://python123.io/ws/demo.html"
#print(get_status(url))


#调用函数爬n次
#for i in range (10):
#    print(get_status("http://www.baidu.com"))

#百度搜索全代码
#def search_baidu(keyword):
#    try:
#        kv = {'wd':keyword}
#        r = requests.get("http://www.baidu.com/s",params = kv)
#        print(r.request.url)
#        r.raise_for_status()
#        print(len(r.text))
#    except:
#        print("error")


#keyword = "Python"
#search_baidu(keyword)


#IP地址查询全代码
#def IP_Search(ipaddress):
#    try:
#        r = requests.get("http://m.ip138.com/ip.asp?ip="+ipaddress)
#        r.raise_for_status()
#        r.encoding = r.apparent_encoding
#        print(r.text[-500:])
#    except:
#        print("Error")

#IP_Search('202.204.80.113')

#demo
#demo = get_status(url)
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(demo,'html.parser')
#print(soup.prettify())
#print(soup.title)
#tag= soup.a
#print(tag.attrs)


#pygame frame
#import pygame,sys
#pygame.init()
#screen = pygame.display.set_mode((600,400))
#while True:
#    for event in pygame.event.get():
#        if event.type ==pygame.QUIT:
#            sys.exit
#    pygame.display.update()
    

# Unit PYG02: Pygame Wall Ball Game version 3  操控型
#import pygame,sys

#pygame.init()
#size = width, height = 600, 400
#speed = [1,1]
#BLACK = 0, 0, 0
#screen = pygame.display.set_mode(size)
#pygame.display.set_caption("Pygame壁球")
#ball = pygame.image.load("little_ball.png")
#ballrect = ball.get_rect()
#fps = 300
#fclock = pygame.time.Clock()

#while True:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            sys.exit()
#        elif event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_LEFT:
#                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1)*int(speed[0]/abs(speed[0]))
#            elif event.key == pygame.K_RIGHT:
#                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
#            elif event.key == pygame.K_UP:
#                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
#            elif event.key == pygame.K_DOWN:
#                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1)*int(speed[1]/abs(speed[1]))
#    ballrect = ballrect.move(speed)
#    if ballrect.left < 0 or ballrect.right > width:
#        speed[0] = - speed[0]
#    if ballrect.top < 0 or ballrect.bottom > height:
#        speed[1] = - speed[1]

#    screen.fill(BLACK)
#    screen.blit(ball, ballrect)
#    pygame.display.update()
#    fclock.tick(fps)


#CrowTaobaoPrice.py
import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"i\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price , title])
    except:
        print("")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))
        
def main():
    goods = '显卡'
    depth = 3
    start_url = 'https://search.jd.com/Search?keyword=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(56*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
    
main()