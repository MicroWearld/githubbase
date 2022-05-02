import turtle as t
from random import choice
porm=[-1,1]
p1_count,p2_count=0,0
#背景
game=t.Screen()
game.title('pingpang v1.0')
game.bgcolor('black')
game.setup(800,600)
#球拍
p1=t.Turtle()
p1.ht()
p1.up()
p1.speed(0)
p1.color('white')
p1.shape('square')
p1.shapesize(5,1)
p1.goto(-350,0)
p1.st()
p2=t.Turtle()
p2.ht()
p2.up()
p2.speed(0)
p2.color('white')
p2.shape('square')
p2.shapesize(5,1)
p2.goto(350,0)
p2.st()
#乒乓
pp=t.Turtle()
pp.up()
pp.speed(0)
pp.color('white')
pp.shape('circle')
#计分板
board=t.Turtle()
board.ht()
board.up()
board.goto(0,180)
board.color('white')
board.write("", align="center",font=("Arial",90))
board.clear()
#速度
pp_cx=5
pp_cy=5
#移动
def p1_up():
    p1.sety(p1.ycor()+20)
def p1_down():
    p1.sety(p1.ycor()-20)
def p2_up():
    p2.sety(p2.ycor()+20)
def p2_down():
    p2.sety(p2.ycor()-20)
def goodbye():
    t.clearscreen()
    t.bye()
#指令
game.listen()
game.onkey(p1_up,'w')
game.onkey(p1_down,'s')
game.onkey(p2_up,'Up')
game.onkey(p2_down,'Down')
game.onkey(goodbye,"q")
while p1_count<3 and p2_count<3:
    pp.setx(pp.xcor()+pp_cx)
    pp.sety(pp.ycor()+pp_cy)
    if pp.ycor()>280 or pp.ycor()<-280:
        pp_cy*=-1
    if pp.ycor()<p1.ycor()+50 and pp.ycor()>p1.ycor()-50 and pp.xcor()<-340:
        pp_cx*=-1
    if pp.ycor()<p2.ycor()+50 and pp.ycor()>p2.ycor()-50 and pp.xcor()>340:
        pp_cx*=-1
    if  -350>pp.xcor():
        p1.color('red')
        pp.home()
        pp_cx*=choice(porm)
        pp_cy*=choice(porm)
        p2_count+=1
        board.clear()
        board.write(f"{p1_count}:{p2_count}", align="center",font=("Arial",90))
        
        #等隔几秒

    if pp.xcor()>350:
        p2.color('red')
        #等个几秒
        pp.home()
        pp_cx*=choice(porm)
        pp_cy*=choice(porm)
        p1_count+=1
        board.clear()
        board.write(f"{p1_count}:{p2_count}", align="center",font=("Arial",90))
        
goodbye()
if p1_count>p2_count:
    print("player1 win!")
else:
    print("player2 win!")
    






