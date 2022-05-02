from tkinter import *
from random import *
import tkinter.messagebox
name=["null"]
already=[]
#姓名读取部分------------------------------------------------------------------------
f=open("name.txt","r",encoding="utf-8")
tmp=f.readline().strip()
while tmp!="":
    name.append(tmp)
    tmp=f.readline().strip()
#end----------------------------------------------------------------------------
def choose():
    global y
    while True:
        x=randint(1,len(name)-1)
        ready=name[x]
        if len(already)==len(name)-1:
            var.set("OVER")
            tkinter.messagebox.showerror(title="please reset!",message="所有人都抽过了,\n请重置!")
            break

        if y.get()==0:
            if not(ready in already):
                var.set(name[x])
                already.append(name[x]) #防止重复抽取
                #print(already)
                break
        else:
            var.set(name[x])
            #print(already)
            break
        
def author():
    tkinter.messagebox.showinfo(title="hello!",message="made by 王辰宇")

def reset():
    global already
    already=[]

def debug():
    def get():
        if e1.get() in name:
            tkinter.messagebox.showerror(message="姓名已存在!")
        else:
            name.append(e1.get())
            l2["text"]=e1.get()+","+"已添加!"

    def delete():
        if not(e1.get() in name):
            tkinter.messagebox.showerror(message="姓名不存在!")
        else:
            name.remove(e1.get())
            l2["text"]=e1.get()+","+"已删除!"
        
    top=Tk()
    v=StringVar()
    v.set("hello!")
    top.title("姓名临时添加或删除")
    top.geometry("250x110")
    top.resizable(False,False)
    l1=Label(top,text="请输入想\n添加或删除:\n的字符串",font=("consolas","9"))
    l2=Label(top)
    e1=Entry(top)
    b2=Button(top,text="添加",command=get,width=5,height=1)
    b3=Button(top,text="删除",command=delete,width=5,height=1)
    l1.place(x=10,y=10,anchor="nw")
    l2.pack(side="bottom")
    e1.place(x=80,y=25,anchor="nw")
    b2.place(x=10,y=70,anchor="nw")
    b3.place(x=190,y=70,anchor="nw")
    top.mainloop()

top=Tk()
var=StringVar()
y=Variable()
var.set("READY")
top.title("姓名抽取")
top.geometry("300x200")
top.resizable(False,False)
l1=Label(top,textvariable=var,font=("consolas","41",'bold'))
b1=Button(top,text="随机抽取",width=15,height=3,command=choose)
b2=Button(top,text="作者",command=author,width=5,height=1)
b3=Button(top,text="重置",command=reset,width=5,height=1)
b4=Button(top,command=debug,width=5,height=1)
r1=Radiobutton(top,text="重复抽取",variable=y,value=1)
r2=Radiobutton(top,text="不重复抽取",variable=y,value=0)
l1.pack()
r1.place(x=5,y=120,anchor="nw")
r2.place(x=210,y=120,anchor="nw")
b1.place(x=94,y=100,anchor="nw")
b2.place(x=20,y=153,anchor="nw")
b3.place(x=235,y=153,anchor="nw")
b4.place(x=127,y=195,anchor="nw")
top.mainloop()
