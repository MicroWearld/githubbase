import turtle
n,a=3,10
lab=turtle.Screen()
lab.delay(0)
while n<=100:
    d=(n-2)*180/n
    t=turtle.Pen()
    t.speed(0)
    for i in range(n):
        t.forward(a)
        t.left(180-d)
    n=n+1
turtle.done()

