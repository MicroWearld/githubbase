from tkinter import *
from random import *
import tkinter.messagebox

a=randint(0,100)
b=randint(0,100)

def com():
    c=int(e1.get())
    if c==a+b:
        tkinter.messagebox.showinfo(title="OK",message="OK")
    else:
        tkinter.messagebox.showerror(title="Fail",message="Wrong!")

top=Tk()
top.title("just a window")
top.resizable(False,False)
top.geometry("210x100")
l1=Label(top,text="输入验证码")
l2=Label(top,text=str(a)+"+"+str(b)+"=?")
e1=Entry(top,show="*")
b1=Button(top,text="确认",command=com)
l1.pack(),l2.pack(),e1.pack(),b1.pack()
top.mainloop()
