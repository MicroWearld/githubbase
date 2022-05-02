from turtle import Turtle, Screen, Terminator, register_shape, Shape
from math import ceil, degrees, atan, pi, e, tau
from tkinter import Menu, Widget, Tk, Button, Entry, Label
import tkinter.messagebox as tmb
from Variable import *

Graph = Screen  # Other name for Screen().
GraphInterrupt = Terminator  # Other name for Terminator.

"This module is developed via turtle,so you can use any option from turtle."

__all__ = ["Graph", "GraphInterrupt", "build_graph",
           "domain", "plot", "legend", "scatter", "setresizable", "setaxis",
           "bar", "legend", "noted", "vsin", "vcos", "vtan"]
__version__ = 1.0
save = [None, None, None]

register_shape("info", Shape(
    "polygon", ((0.00, 0.00), (-4, 10.00), (0, 0), (4, 10), (0, 0), (0, 16))))


class DomainError(Exception):
    "Other name for IndexError."


class Arrow(Turtle):
    "Other name for Turtle."

    def __init__(self, Label=None, color="orange", psize=2, size=1, speed=5, mark="classic",
                 ana=False):
        super().__init__()
        self.color(color)
        self.pensize(psize)
        self.speed(speed)
        self.shape(mark)
        self.shapesize(size)
        self.label = Label
        self.color = color
        if ana:
            self.st()
        else:
            self.ht()
        self.speed1 = self.speed()

    def draw(self, x, y, turn=True):
        "Draw the data."
        self.speed(0)
        if turn:
            if x == self.xcor():
                deg = 90
            else:
                deg = degrees(atan((y - self.ycor()) / (x - self.xcor())))
            if x < self.xcor():
                deg += 180
            elif x == self.xcor() and y < self.ycor():
                deg += 180
            deg = deg - self.heading()
            self.left(deg)
        self.speed(self.speed1)
        self.goto(x, y)


def build_graph(screen, lim, per, le, delay=0, ruler=[True, True], label=["x", "y"], obje=True):
    def clickon(tur, x, y):
        tur.clear()
        tur.goto(x, y)
        tur.write(tur.pos(), align="right")

    global xline, yline, save
    "Build graphfic screen."
    screen.delay(0)
    screen.title("pyGraphic plot")
    x = lim[0] / 2
    y = lim[1] / 2
    xline = Turtle()
    xline.write(" 0", align="left")
    yline = Turtle()
    for line in [xline, yline]:
        line.ht()
        line.up()
        line.speed(0)
    xline.goto(-x, 0)
    yline.goto(0, -y)
    xline.down()
    yline.down()
    yline.lt(90)
    for i in range(ceil(lim[0] // per[0])):
        if ruler[0] and xline.xcor() != 0:
            xline.write(round(xline.xcor(), 2))
        xline.fd(per[0])
        xx = xline.xcor()
        xy = xline.ycor()
        xline.goto(xx, xy + le[0])
        xline.goto(xx, xy)
    for i in range(ceil(lim[1] // per[1])):
        if ruler[1] and yline.ycor() != 0:
            yline.write(round(yline.ycor(), 2), align="right")
        yline.fd(per[1])
        yx = yline.xcor()
        yy = yline.ycor()
        yline.goto(yx + le[1], yy)
        yline.goto(yx, yy)
    xline.st()
    yline.st()
    xline.write(label[0], align="left", font=(10,))
    yline.write(label[1], align="left", font=(10,))
    screen.delay(delay)
    save[0], save[1], save[2] = lim, ruler, label
    _setop(screen)
    if obje:
        click = Turtle()
        click.color("black")
        click.shape("info")
        click.shapesize(.8)
        click.seth(90)
        click.up()
        screen.onscreenclick(lambda r1, r2: clickon(click, r1, r2), 1)


def _setop(tk):
    def world(e1, e2, e3, e4, e5, e6):
        try:
            x, y, lx, ly, dx, dy = float(e1.get()), float(e4.get()), float(
                e2.get()), float(e5.get()), float(e3.get()), float(e6.get())
        except ValueError:
            tmb.showerror(title="错误", message="无效参数!!!")
        else:
            xline.clear()
            yline.clear()
            setaxis(tk, x, y, lx, ly)
            build_graph(tk, save[0], [dx, dy], [ly / 100, lx / 100],
                        ruler=save[1], label=save[2], obje=False)

    def dele(e1, e2, e3, e4, e5, e6):
        for i in [e1, e2, e3, e4, e5, e6]:
            i.delete(0, len(i.get()))

    def hhheeelllppp():
        m = '中心横坐标：视野中心的横坐标\n' + '中心纵坐标：视野中心的纵坐标\n'\
            + '横轴视距：视野中心到横向边界的距离\n' + '纵轴视距：视野中心到纵向边界的距离\n'\
            + '横轴刻度：横轴的最小刻度值\n' + '纵轴刻度：纵轴的最小刻度值'
        tmb.showinfo(title="帮助", message=m)

    def hello():
        tmb.showinfo(title="你好!", message="本模块由高二(3)班王辰宇一人完成")

    def changegeraph():
        top = Tk()
        top.title("图像设置")
        top.geometry("377x100")
        top.resizable(0, 0)
        commit = Button(top, text="确认", width=8,
                        command=lambda: world(ex1, ex2, ex3, ey4, ey5, ey6))
        delete = Button(top, text="清除", command=lambda: dele(
            ex1, ex2, ex3, ey4, ey5, ey6), width=8)
        helpd = Button(top, text="帮助", command=hhheeelllppp, width=8)
        ex1, ex2, ex3, ey4, ey5, ey6 = [Entry(top, width=8) for i in range(6)]
        lx1, lx2, lx3, ly4, ly5, ly6 = Label(top, text="中心横坐标", width=8), Label(top, text="横轴视距", width=8), Label(
            top, text="横轴刻度", width=8), Label(top, text="中心纵坐标", width=8), Label(top, text="纵轴视距", width=8), Label(top, text="纵轴刻度", width=8)
        E = [lx1, ex1, lx2, ex2, lx3, ex3, ly4, ey4, ly5, ey5, ly6, ey6]
        for i in range(2):
            for j in range(6):
                E[i * 6 + j].grid(row=i, column=j, sticky="e")
        commit.grid(row=3, column=2, columnspan=2, pady=12)
        delete.grid(row=3, column=0, pady=12)
        helpd.grid(row=3, column=5, pady=12)

    root = getroot(tk)
    setting = Menu(root)
    setting.add_command(label="图像设置", command=changegeraph)
    setting.add_command(label="关于", command=hello)
    root.config(menu=setting)


def domain(start, end, step):
    "Set your 'x' from start to end,which setp is step(defination of domain)."
    lis = []
    c = start
    while c < end:
        lis.append(c)
        c += step
    return Variable(*tuple(lis))


def legend(graph, pos, font=None):
    "Show label you set."
    comment = Turtle()
    comment.ht()
    comment.up()
    comment.goto(pos[0], pos[1])
    c = 0
    for arrows in graph.turtles()[::-1]:
        if type(arrows) is Arrow:
            comment.color(arrows.color)
            comment.write(arrows.label + "\n" * c, font=font)
            c += 1


def noted(pos, note, c="black", font=None):
    comment = Turtle()
    comment.color(c)
    comment.ht()
    comment.up()
    comment.goto(pos[0], pos[1])
    comment.write(note, font=font)
    return comment


def plot(x_axis_data, y_axis_data, c="orange", ps=2, s=1, v=1, Label=None, label=False, ana=True):
    "Draw data as line."
    arrow = Arrow(Label=Label, color=c, psize=ps, size=s,
                  speed=v, mark="classic", ana=ana)
    c = 0
    arrow.penup()
    try:
        arrow.goto(x_axis_data[0], y_axis_data[0])
    except IndexError:
        raise DomainError("Empty domain,please check your code!")
    if label:
        arrow.write(arrow.pos())
    arrow.pendown()
    for i in range(1, len(x_axis_data)):
        arrow.draw(x_axis_data[i], y_axis_data[i])
        if label:
            if c % 500 == 0:
                arrow.write(arrow.ycor())
            c += 1
    return arrow


def scatter(x_axis_data, y_axis_data, c, s=0.3, marker="circle", v=0):
    "draw data as dot."
    arrow = Arrow(color=c, size=s, speed=v, mark=marker, ana=True)
    arrow.penup()
    for i in range(len(x_axis_data)):
        arrow.draw(x_axis_data[i], y_axis_data[i], turn=False)
        arrow.stamp()
    return arrow


def bar(x_axis_data, y_axis_data, c, labelpos, v=0, font=("Terminal", 14)):
    def _drawsquare(turtle, fillcolor, distance):
        turtle.fillcolor(fillcolor)
        turtle.begin_fill()
        turtle.left(90)
        turtle.forward(distance)
        turtle.right(90)
        turtle.forward(0)
        turtle.forward(1)
        turtle.right(90)
        turtle.forward(distance)
        turtle.left(90)
        turtle.end_fill()

    arrow = Arrow(color="black", psize=1, speed=v, ana=False)
    for i in range(len(x_axis_data)):
        arrow.up()
        arrow.goto(arrow.xcor() + labelpos[0], arrow.ycor() - labelpos[1])
        y = y_axis_data[i]
        arrow.write(x_axis_data[i], font=font, align="center")
        arrow.goto(arrow.xcor() - labelpos[0], arrow.ycor() + labelpos[1])
        arrow.down()
        _drawsquare(arrow, c, y)

    return arrow


def setresizable(graph, resizable=(0, 0)):
    "Other name for resizeable"
    graph.getcanvas().master.resizable(*resizable)


def setaxis(graph, x, y, lx, ly):
    "Other name for setworldcoordinates."
    llx = x - lx
    lly = y - ly
    urx = x + lx
    ury = y + ly
    graph.setworldcoordinates(llx, lly, urx, ury)


def getroot(graph):
    "Get graph root window."
    return graph.getcanvas().master
