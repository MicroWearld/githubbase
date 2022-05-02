import turtle
n=int(input("input:"))
a=int(input("input:"))
d=(n-2)*180/n
t=turtle.Pen()
for i in range(n):
    t.forward(a)
    t.left(180-d)
turtle.done()

