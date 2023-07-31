from tkinter import *
import tkinter.messagebox
from functools import partial
from core import check


class Mbutton(Button):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__()
        Widget.__init__(self, master, 'button', cnf, kw)
        self.pos = ""


def judge(butt):
    global turn
    L1["text"] = f"玩家{turn%2+1}落子..."
    L2["text"] = ""
    i, j = list(map(int, butt.pos.split(",")))
    if sq[j][i] != 0:
        L2["text"] = "该位置已有棋子!"
        L2["fg"] = "red"
        return None
    else:
        if turn % 2 == 0:
            butt["text"] = "X"
            sq[j][i] = turn % 2+1
        else:
            butt["text"] = "O"
            sq[j][i] = turn % 2+1
        turn += 1
    if not check(sq):
        for buon in l:
            buon["state"] = "disabled"
        tkinter.messagebox.showinfo(message=f"玩家{j%2+1}获胜!\n游戏结束,请重置!")


def restart():
    global sq, turn
    for i in l:
        i["text"] = ""
    for row1 in range(len(sq)):
        for column1 in range(len(sq[0])):
            sq[row1][column1] = 0
    for buon in l:
        buon["state"] = "normal"
    turn = 1
    L2["fg"] = "black"
    L2["text"] = "重置完毕!"
    L1["text"] = "玩家1落子..."


l = []
row, column = 15, 15
turn = 1
sq = [[0 for i in range(column)] for j in range(row)]
root = Tk()
root.resizable(False, False)
root.geometry("460x500")
root.title("五子棋")
L1 = Label(root, text="玩家1落子...", font=("consolas", "15"))
L2 = Label(root, text="", font=("consolas", "15"))
rB = Button(root, text="重置", command=restart, width=10, height=1)
L1.place(anchor="nw", x=3, y=465)
L2.place(anchor="nw", x=200, y=465)
rB.place(anchor="nw", x=370, y=463)

for i in range(1, row*column+1):
    a = Mbutton(root, text="", width=3, height=1)
    a["command"] = partial(judge, a)
    l.append(a)
for i in range(column):
    for j in range(row):
        l[i*row+j].pos = f"{j},{i}"
        l[i*row+j].place(anchor="nw", x=5+j*30, y=5+i*30)

root.mainloop()
