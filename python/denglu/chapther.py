#这是验证码模块-----------------------------------------------------------------

import turtle
from random import *

def chapther(a):
    turtle.setup(450,200)
    p=turtle.Pen()
    x=-200
    y=50
    match=0
    col=["red","blue","yellow","green","purple","black","orange"]
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
    
    num=str(a)
    p.penup()
    for i in range(len(num)):
        t=int(num[i])
        if t==1:
            p_t()
            p_6()
            p_7()
            p_l()

        elif t==2:
            p_1()
            p_2()
            p_3()
            p_t()
            p_5()
            p_6()
            p_l()

        elif t==3:
            p_1()
            p_2()
            p_3()
            p_t()
            p_6()
            p_7()
            p_l()

        elif t==4:
            p_2()
            p_t()
            p_4()
            p_6()
            p_7()
            p_l()

        elif t==5:
            p_1()
            p_2()
            p_3()
            p_t()
            p_4()
            p_7()
            p_l()

        elif t==6:
            p_1()
            p_2()
            p_3()
            p_t()
            p_4()
            p_5()
            p_7()
            p_l()

        elif t==7:
            p_1()
            p_t()
            p_6()
            p_7()
            p_l()

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

        elif t==9:
            p_1()
            p_2()
            p_3()
            p_t()
            p_4()
            p_6()
            p_7()
            p_l()

        elif t==0:
            p_1()
            p_3()
            p_t()
            p_4()
            p_5()
            p_6()
            p_7()
            p_l()

        x=x+90

    turtle.clearscreen()
    turtle.bye()
    
#如果想要测试,删掉以下代码的"#"
#chapther()
