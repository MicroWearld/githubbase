from tkinter import *
import tkinter.messagebox
from random import *

a=randint(0,100)
b=randint(0,100)

def denglu():
    usr=e1.get()
    pas=e2.get()
    if usr=="wang" and pas=="123":
        tkinter.messagebox.showinfo(title="correct",message="成功")
    else:
        tkinter.messagebox.showerror(title="fail",message="用户名或密码不正确")

def zhuce():
    x=e3.get()
    if x==a+b:
        Ousr=e1.get()
        Opas=e2.get()
        tkinter.messagebox.showinfo(message="注册成功")
    else:
        tkinter.messagebox.showerror(message="验证码错误")
        
    
        
top=Tk()
top.title("注册界面")
#top.resizable(False,False)
top.geometry("210x200")
l1=Label(top,text="注册",)
l2=Label(top,text="用户名")
l3=Label(top,text="密码")
l4=Label(top,text="请输入验证码:"+"\n"+str(a)+"+"+str(b)+"=?")
#z1=Label(top)
e1=Entry(top)
e2=Entry(top,show="*")
e3=Entry(top)
b1=Button(top,text="登陆",command=zhuce)
l1.pack()
l2.pack()
e1.pack()
#z1.pack()
l3.pack()
e2.pack()
l4.pack()
e3.pack()
b1.pack()
top.mainloop
