from phylib import *
from time import sleep
from decimal import Decimal
pi=m.pi
bitsec=2**10
lab=t.Screen()
build_lab(lab,1200,1200,50,0,ruler=True)
o1=pobject([-250,0],"square",[10,10],speed=1)
o1.setmass(1)
o1.setlimt(0)
o1.setf0(10,-pi/2)
o1.setv0(10,0)
o1.down()
for i in range(10000):
    o1.goto(o1.cacul(1))
