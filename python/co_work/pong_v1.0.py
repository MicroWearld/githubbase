#乒乓球游戏
#核心与设计：费仲勋
#算法与代码优化：王辰宇
#玩法请细看运行后的提示
import os
import turtle as t
import time
from random import choice
class hitbox(t.Turtle):#碰撞箱定义
    def __init__(self,shapex,shapey,x,y,color):
        super().__init__()
        self.by=shapex*20+1
        self.bx=shapey*20+1
        self.ht()
        self.shape("square")
        self.shapesize(shapex,shapey)
        self.color(color)
        self.up()
        self.speed(0)
        self.goto(x,y)
        self.st()

class board(t.Turtle):#信息板定义
    def __init__(self,x,y,color):
        super().__init__()
        self.ht()
        self.up()
        self.goto(x,y)
        self.color(color)
        
def hitcheck(tb1,tb2):#碰撞检测
    f1=f2=False
    bx=(tb1.bx+tb2.bx)/2
    by=(tb1.by+tb2.by)/2
    if tb1.xcor()-bx<=tb2.xcor()<=tb1.xcor()+bx:
        f1=True
    if tb1.ycor()-by<=tb2.ycor()<=tb1.ycor()+by:
        f2=True
    return f1 and f2

#随机发球和比分设置
porm=[-1,1]
p1_count,p2_count=0,0
#背景
game=t.Screen()
game.title('pong v1.0')
game.bgcolor('black')
game.setup(800,600)
#球拍
p1=hitbox(5,1,-350,0,"white")
p2=hitbox(5,1,350,0,"white")
pb=[p1,p2]
#乒乓
pp=hitbox(1,1,0,0,"orange")
#信息板
cboard=board(0,180,"white")
cboard.write(f"{p1_count}:{p2_count}",align="center",font=("Terminal",90))
start=board(0,0,"white")
end=board(0,0,"white")
comment1=board(0,-50,"white")
comment2=board(0,-70,"white")
use1=board(-275,-80,"white")
use2=board(275,-80,"white")
speed=board(0,170,"white")
#速度
pp_cx=4
pp_cy=2
vp=50
v=0.125
def limv(v):
    if abs(pp_cx)>6:
        return 0
    else:
        return v
#移动
def p1_up():
    if p1.ycor()<250:
        p1.sety(p1.ycor()+vp)
def p1_down():
    if p1.ycor()>-250:
        p1.sety(p1.ycor()-vp)
def p2_up():
    if p2.ycor()<250:
        p2.sety(p2.ycor()+vp)
def p2_down():
    if p2.ycor()>-250:
        p2.sety(p2.ycor()-vp)
#开始结束
def goodbye():
    game.clearscreen()
    t.bye()
def reset():
    global p1_count,p2_count,pp_cx
    pp_cx=4
    p1_count,p2_count=0,0
    pp.home()
    p1.goto(-350,0)
    p2.goto(350,0)
    cboard.clear();comment1.clear();comment2.clear();end.clear();speed.clear()
    cboard.write(f"{p1_count}:{p2_count}",align="center",font=("Terminal",90))
    main()
#指令
game.listen()
start.write("PONG v1.0",align="center",font=("Terminal",90))
comment1.write("Press <g> to start!",align="center",font=("Terminal",20))
use1.write("Player1\nuse <w> and <s> to control",align="center",font=("Terminal",10))
use2.write("Player2\nuse <Up> and <Down> to control",align="center",font=("Terminal",10))
game.delay(1)
def main():
    global p1_count,p2_count,pp_cx,pp_cy
    game.onkey(p1_up,'w')
    game.onkey(p1_down,'s')
    game.onkey(p2_up,'Up')
    game.onkey(p2_down,'Down')
    start.clear();comment1.clear();use1.clear();use2.clear()
    speed.write(f"speed:{abs(round(pp_cx,2))}",align="center",font=("Terminal",15))
    time.sleep(1)
    while p1_count<3 and p2_count<3:
        pp.goto(pp.xcor()+pp_cx,pp.ycor()+pp_cy)
        if pp.ycor()>280 or pp.ycor()<-280:
            pp_cy*=-1
        for pobj in pb:
            if hitcheck(p1,pobj):
                if pp_cx>0:
                    pp_cx+=limv(v)
                else:
                    pp_cx-=limv(v)
                if pp.ycor()-pobj.ycor()==0 or (pp.bx+pobj.bx)/(pp.by+pobj.by)<abs(pp.xcor()-pobj.xcor())/abs(pp.ycor()-pobj.ycor()):
                    pp_cx*=-1
                elif pp.ycor()-pobj.ycor()!=0 and(pp.bx+pobj.bx)/(pp.by+pobj.by)>abs(pp.xcor()-pobj.xcor())/abs(pp.ycor()-pobj.ycor()):
                    pp_cy*=-1
                else:
                    pp_cx*=-1;pp_cy*=-1
                speed.clear()
                speed.write(f"speed:{abs(round(pp_cx,2))}",align="center",font=("Terminal",15))
    
        if  -380>pp.xcor():
            p1.color('red')
            pp.home()
            p1.goto(-350,0);p2.goto(350,0)
            pp_cx*=choice(porm)
            pp_cy*=choice(porm)
            p2_count+=1
            cboard.clear()
            cboard.write(f"{p1_count}:{p2_count}",align="center",font=("Terminal",90))
            time.sleep(1)
            pp_cx=4
            speed.clear()
            speed.write(f"speed:{abs(round(pp_cx,2))}",align="center",font=("Terminal",15))
            p1.color('white')

        if pp.xcor()>380:
            p2.color('red')
            pp.home()
            p1.goto(-350,0);p2.goto(350,0)
            pp_cx*=choice(porm)
            pp_cy*=choice(porm)
            p1_count+=1
            cboard.clear()
            cboard.write(f"{p1_count}:{p2_count}", align="center",font=("Terminal",90))
            time.sleep(1)
            pp_cx=4
            speed.clear()
            speed.write(f"speed:{abs(round(pp_cx,2))}",align="center",font=("Terminal",15))
            p2.color('white')
            
    if p1_count>p2_count:
        end.write("Player1 win!",align="center",font=("Terminal",80))
    else:
        end.write("Player2 win!",align="center",font=("Terminal",80))
    comment2.write("Press <q> to quit\nPress <r> to restart",align="center",font=("Terminal",20))

game.onkey(goodbye,"q")
game.onkey(reset,"r")
game.onkey(main,"g")
game.mainloop()
