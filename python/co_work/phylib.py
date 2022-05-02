import turtle as t
import math as m

class pobject(t.Turtle):
    def __init__(self,pos,shp,bsz,speed=2):
        super().__init__()
        self.by=bsz[0]
        self.bx=bsz[1]
        self.shape(shp)
        self.speed(speed)
        self.ht()
        self.px,self.py=pos[0],pos[1]
        self.up()
        self.goto(self.px,self.py)
        self.shapesize(bsz[0]/20,bsz[1]/20)
        self.st()

    def setlimt(self,limt=0):
        self.limt=limt
        self.time=self.limt
        
    def setmass(self,mass):
        self.mass=mass
        self.px=self.xcor();self.py=self.ycor()

    def setf0(self,f0=0,radf=0):
        self.f0=f0
        self.radf=radf
        self.time=self.limt
        self.px=self.xcor();self.py=self.ycor()

    def setv0(self,v0=0,radv=0):
        self.v0=v0
        self.radv=radv
        self.time=self.limt
        self.px=self.xcor();self.py=self.ycor()

    def cacul(self,time):
        self.time+=time
        self.ax=m.cos(self.radf)*(self.f0/self.mass)
        self.ay=m.sin(self.radf)*(self.f0/self.mass)
        self.vx=m.cos(self.radv)*self.v0
        self.vy=m.sin(self.radv)*self.v0    
        x=self.vx*self.time+0.5*self.ax*self.time**2
        y=self.vy*self.time+0.5*self.ay*self.time**2
        return self.px+x,self.py+y

class field(pobject):
    def __init__(self,pos,shp,bsz,name,col):
        super().__init__(pos,shp,bsz)
        self.speed(0)
        self.ht();self.pensize(3)
        self.goto(self.px-self.bx/2,self.py-self.by/2)
        self.color(col)
        self.down()
        for k in range(2):
            self.fd(self.bx)
            self.left(90)
            self.fd(self.by)
            self.left(90)
        self.up()
        self.goto(self.px,self.py)
        self.write(name,align="center",font=("Terminal",20))

class massdot(t.Turtle):
    def __init__(self,pos,color="black"):
        super().__init__()
        self.ht()
        self.px,self.py=pos[0],pos[1]
        self.up()
        self.goto(self.px,self.py)
        self.shape("circle")
        self.shapesize(0.2,0.2)
        self.color(color)
        self.st()

class board(t.Turtle):
    def __init__(self,pos,color,font):
        super().__init__()
        self.up();self.speed(0)
        self.goto(pos[0],pos[1])
        self.color(color)
        self.font=font
        self.ht()
    
    def draw(self,comment,align):
        self.write(comment,align=align,font=self.font)

def hitcheck(tb1,tb2):#碰撞检测
    f1=f2=False
    bx=(tb1.bx+tb2.bx)/2
    by=(tb1.by+tb2.by)/2
    if tb1.xcor()-bx<=tb2.xcor()<=tb1.xcor()+bx:
        f1=True
    if tb1.ycor()-by<=tb2.ycor()<=tb1.ycor()+by:
        f2=True
    return f1 and f2

def build_lab(screen,limx,limy,per,delay=1,ruler=True):
    screen.screensize(limx,limy)
    screen.delay(0)
    x=limx/2;y=limy/2
    xline=t.Turtle();yline=t.Turtle()
    xline.ht();yline.ht();xline.up();yline.up()
    xline.speed(0);yline.speed(0)
    xline.goto(-x,0);yline.goto(0,-y)
    xline.down();yline.down()
    yline.lt(90)
    for i in range(limx//per):
        if ruler:
            xline.write(xline.xcor())
        xline.fd(per)
        xx=xline.xcor();xy=xline.ycor()
        xline.goto(xx,xy+3)
        xline.goto(xx,xy)
    for i in range(limy//per):
        if ruler:
            yline.write(yline.ycor())
        yline.fd(per)
        yx=yline.xcor();yy=yline.ycor()
        yline.goto(yx+3,yy)
        yline.goto(yx,yy)
    xline.st();yline.st()
    xline.write("x",align="left",font=(10,))
    yline.write("y",align="left",font=(10,))
    screen.delay(delay)
