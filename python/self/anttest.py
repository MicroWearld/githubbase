import turtle as tt
from progressbar import pgbar

n=int(input("input int:"))
mapp=[];mapp1=[]
mapp=[[0 for a1 in range(3)]for a2 in range(n)]
mapp1=[[0 for a1 in range(3)]for a2 in range(n)]
a=10 #行程长短
i,test=0,0
# 1==black;0==white
s=tt.Screen()
s.delay(0)
t=tt.Pen()
t.shape("classic")
t.shapesize(0.5)
t.speed(0)
t.pensize(1)
#t.hideturtle()
class ant:
    def __init__(self,x,y,arg,color):
        self.x=x
        self.y=y
        self.arg=check(arg)
        self.color=color
    def step(self):
        if self.arg==0 or self.arg==360:
            self.x+=1
        elif self.arg==90:
            self.y+=1
        elif self.arg==180:
            self.x-=1
        elif self.arg==270:
            self.y-=1
        else:
            print("error!")
    def turn(self):
        if self.color==1:
            self.arg+=90
            self.arg=check(self.arg)
        else:
            self.arg-=90
            self.arg=check(self.arg)
    def change(self,ncolor):
        self.color=ncolor
    def describe(self):
        print("ant:",f"x={self.x}",f"y={self.y}",f"arg={self.arg}",f"color={self.color}")

def check(q):
    while q < 0 or q > 360:
        if q > 360:
            q -= 360
        elif q < 0:
            q += 360
    return q

def move(pen,a,color):
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(4):
        pen.forward(a)
        pen.right(90)
    pen.end_fill()

ant1=ant(0,0,0,0)
pb1=pgbar(20)
pb2=pgbar(20,True)
#ant1.describe()
print("start mapping!")
while i<n:
    pb1.rise(i,n)
    if len(mapp)!=0:
        for j in range(len(mapp)):
            if ant1.x==mapp[j][0] and ant1.y==mapp[j][1]:
                if mapp[j][2]==1:
                    ant1.change(1)
                    mapp[j][2]=0
                    break
                else:
                    ant1.change(0)
                    mapp[j][2]=1
                    break
            else:
                pass
    ant1.turn()
    ant1.step()
    #ant1.describe()
    mapp[i][0],mapp[i][1]=ant1.x,ant1.y
    mapp1[i][0],mapp1[i][1]=ant1.x,ant1.y
    i+=1

print("end mapping!")
print("paint start!")
for b in mapp:
    pb2.rise(test,n)
    if b[2]==0:
        move(t,a,"white")
    else:
        move(t,a,"black")
    t.goto(b[0]*a,b[1]*a)
    test+=1
print("paint end!")
print(mapp)
s.mainloop()
