import turtle
from random import *

p=turtle.Pen()
x=-200
y=100
match=0
col=["red","blue","yellow","green","purple","pink","gray","black","brown","orange"]
p.pensize(5)
p.speed(2)


def p_t():
    p.pencolor(choice(col))
    p.right(90)
    
def p_l():
    p.pencolor(choice(col))
    p.left(90)

def p_1():
    p.pencolor(choice(col))
    p.goto(x,y)
    p.pendown()
    p.forward(50)
    p.penup()
    
def p_2():
    p.pencolor(choice(col))
    p.goto(x,y-50)
    p.pendown()
    p.forward(50)
    p.penup()

def p_3():
    p.pencolor(choice(col))
    p.goto(x,y-100)
    p.pendown()
    p.forward(50)
    p.penup()

def p_4():
    p.pencolor(choice(col))
    p.goto(x,y)
    p.pendown()
    p.forward(50)
    p.penup()

def p_5():
    p.pencolor(choice(col))
    p.goto(x,y-50)
    p.pendown()
    p.forward(50)
    p.penup()

def p_6():
    p.pencolor(choice(col))
    p.goto(x+50,y)
    p.pendown()
    p.forward(50)
    p.penup()

def p_7():
    p.pencolor(choice(col))
    p.goto(x+50,y-50)
    p.pendown()
    p.forward(50)
    p.penup()
    
num=input("A number:")
p.penup()
for i in range(len(num)):
    t=int(num[i])
    if t==1:
        p_t()
        p_6()
        p_7()
        p_l()
        match=match+2
        print(match)
    
    elif t==2:
        p_1()
        p_2()
        p_3()
        p_t()
        p_5()
        p_6()
        p_l()
        match=match+5
        print(match)

    elif t==3:
        p_1()
        p_2()
        p_3()
        p_t()
        p_6()
        p_7()
        p_l()
        match=match+5
        print(match)

    elif t==4:
        p_2()
        p_t()
        p_4()
        p_6()
        p_7()
        p_l()
        match=match+4
        print(match)

    elif t==5:
        p_1()
        p_2()
        p_3()
        p_t()
        p_4()
        p_7()
        p_l()
        match=match+5
        print(match)

        
    elif t==6:
        p_1()
        p_2()
        p_3()
        p_t()
        p_4()
        p_5()
        p_7()
        p_l()
        match=match+6
        print(match)

    elif t==7:
        p_1()
        p_t()
        p_6()
        p_7()
        p_l()
        match=match+3
        print(match)

    elif t==8:
        p_1()
        p_2()
        p_3()
        p_t()
        p_4()
        p_5()
        p_6()
        p_7()
        p_l()
        match=match+7
        print(match)

    elif t==9:
        p_1()
        p_2()
        p_3()
        p_t()
        p_4()
        p_6()
        p_7()
        p_l()
        match=match+6
        print(match)

    elif t==0:
        p_1()
        p_3()
        p_t()
        p_4()
        p_5()
        p_6()
        p_7()
        p_l()
        match=match+6
        print(match)

    x=x+90
