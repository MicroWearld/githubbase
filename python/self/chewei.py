from tkinter import *


def check():
    if e.get() == "1":
        var1.set("绿色")
        l3["fg"] = "green"
        var2.set("空车位")
    elif e.get() == "0":
        var1.set("红色")
        l3["fg"] = "red"
        var2.set("非空车位")
    else:
        var1.set("NONE")
        l3["fg"] = "black"
        var2.set("NONE")


top = Tk()
var1, var2 = StringVar(), StringVar()
var1.set("NONE")
var2.set("NONE")
top.title("车位探测及处理")
top.geometry("310x200")
top.resizable(False, False)
l1 = Label(top, text="输入车位状态值:", font=("consolas", "12"))
l2 = Label(top, text="车位上方指示灯颜色：", font=("consolas", "12"))
l3 = Label(top, textvariable=var1, font=("consolas", "12"), fg="black")
l4 = Label(top, text="车位状态：", font=("consolas", "12"))
l5 = Label(top, textvariable=var2, font=("consolas", "12"))
e = Entry(top, width=4)
b = Button(top, text="确定", command=check, width=4, height=1)
l1.place(x=30, y=19, anchor="nw")
l2.place(x=30, y=90, anchor="nw")
l3.place(x=200, y=90, anchor="nw")
l4.place(x=30, y=150, anchor="nw")
l5.place(x=200, y=150, anchor="nw")
e.place(x=175, y=20, anchor="nw")
b.place(x=225, y=17, anchor="nw")
top.mainloop()
