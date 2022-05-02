from tkinter import *
from random import *
import tkinter.messagebox
fx=open("zhongzhuan.txt","w")
def test():
    def get():
        if e1.get() in name:
            tkinter.messagebox.showerror(message="姓名已存在!")
        else:
            fx.write(e1.get())
            var.set(e1.get()+","+"已添加!")

    def delete():
        if not(e1.get() in name):
            tkinter.messagebox.showerror(message="姓名不存在!")
        else:
            fx.write(e1.get())
            var.set(e1.get()+","+"已删除!")
            
    top=Tk()
    var=StringVar()
    var.set("......")
    top.title("DEBUG MODE")
    top.geometry("250x110")
    top.resizable(False,False)
    l1=Label(top,text="请输入想\n添加或删除:\n的字符串",font=("consolas","9"))
    l2=Label(top,textvariable=var)
    e1=Entry(top)
    b2=Button(top,text="添加",command=get,width=5,height=1)
    b3=Button(top,text="删除",command=delete,width=5,height=1)
    l1.place(x=10,y=10,anchor="nw")
    l2.pack(side="bottom")
    e1.place(x=80,y=25,anchor="nw")
    b2.place(x=10,y=70,anchor="nw")
    b3.place(x=190,y=70,anchor="nw")
    top.mainloop()
