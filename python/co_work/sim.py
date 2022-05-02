from phylib import *
from time import sleep
from decimal import Decimal
pi=m.pi
bitsec=2**10
lab=t.Screen()
build_lab(lab,1200,1200,50,0,ruler=True)
o1=pobject([-250,0],"square",[10,10],speed=0)
o1.pensize(1)
mf=field([0,0],"square",[1200,1200],name="B=2T",col="blue")
o1.color("red")
o1.setlimt(0)
o1.setmass(1)
#------------------------------
m=1
v=bitsec*10
sita=0
q=-5
B=2
Fl=B*q*v
r=m*v/(B*q)
omega=v/r
#------------------------------
o1.setf0(0,0)
o1.setv0(v,sita)
o1.down()
lab.listen()
def gb():
    lab.bye()
def forward():
    global sita
    if hitcheck(o1,mf):
        sita+=1/omega
        o1.f0=Fl
        o1.radf=pi/2-sita
    o1.goto(o1.cacul(1/bitsec))

def back():
    global sita
    print(sita,pi/2+sita)
    if hitcheck(o1,mf):
        sita-=1/omega
        o1.setv0(v,sita)
        #o1.setf0(Fl,pi/2+sita)
    o1.goto(o1.cacul(-1/bitsec))

lab.onkeypress(forward,"f")
lab.onkeypress(back,"b")
lab.onkey(gb,"q")
lab.mainloop()
