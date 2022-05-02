#python D:\IT\python\project\win.py
from tkinter import *
import tkinter.messagebox
from random import *
import chapther as cp

f1=open("username.txt", "r")
f2=open("password.txt", "r")
Ousr,Opas=f1.readline().strip(),f2.readline().strip()
alo=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
f,de=0,0
f1.close()
f2.close()

def denglu():
    f1=open("username.txt", "r")
    f2=open("password.txt", "r")
    Ousr,Opas=f1.readline().strip(),f2.readline().strip()
    usr=e1.get()
    pas=e2.get()
    tmp=False
    while Ousr!="" and Opas!="":
        if usr==Ousr and pas==Opas:
            tmp=True
            break
        else:
            Ousr,Opas=f1.readline().strip(),f2.readline().strip()
            continue
    if tmp:
        tkinter.messagebox.showinfo(title="correct",message="登入成功")
    else:
        tkinter.messagebox.showerror(title="error",message="用户名或密码错误!")
    f1.close()
    f2.close()

def zhuce():
    a=randint(1000, 9999)
    #a=9999
    def chap():
        global f
        if f==0:
            cp.chapther(a)
            f=1
        else:
            tkinter.messagebox.showerror(message="验证码只能显示一次")

    def zhuc():
        global Ousr,Opas,i,de
        f1=open("username.txt", "r")
        f2=open("password.txt", "r")
        Ousr,Opas=f1.readline().strip(),f2.readline().strip()
        i=0
        x=e3.get()
        for y in range(len(x)):
            if not (x[y] in alo):
                i+=1
        if i!=0 or x=="":
            tkinter.messagebox.showerror(message="格式错误")
            de=0
        else:
            x=int(x)
            if x==a:
                Ou=e1.get()
                Op=e2.get()
                tmp=True
                while Ousr!="" and Opas!="":
                    if Ou==Ousr or Op==Opas:
                        tmp=False
                        break
                    else:
                        Ousr,Opas=f1.readline().strip(),f2.readline().strip()
                        continue
                f1.close()
                f2.close()
                if tmp:
                    f1=open("username.txt","a")
                    f2=open("password.txt","a")
                    tkinter.messagebox.showinfo(message="注册成功")
                    f1.write("\n"+Ou)
                    f2.write("\n"+Op)
                    f1.close()
                    f2.close()
                    top.destroy()
                else:
                    tkinter.messagebox.showinfo(message="用户名或密码已被使用！")
            else:
                tkinter.messagebox.showerror(message="验证码错误")

    top=Tk()
    top.title("注册界面")
    top.resizable(False, False)
    top.geometry("310x220")
    l1=Label(top,text="注册",font=("consolas","30",'bold italic'))
    l2=Label(top,text="用户名:")
    l3=Label(top,text="密码:")
    l4=Label(top,text="请输入验证码:")
    e1=Entry(top)
    e2=Entry(top,show="*")
    e3=Entry(top)
    b1=Button(top,text="注册",command=zhuc,width=12,height=2)
    b2=Button(top,text="获取验证码",command=chap,width=12,height=2)
    l1.pack()
    l2.place(x=57,y=48,anchor='nw')
    e1.place(x=109,y=48,anchor='nw')
    l3.place(x=60,y=90,anchor='nw')
    e2.place(x=109,y=90,anchor='nw')
    l4.place(x=18,y=135,anchor='nw')
    e3.place(x=109,y=135,anchor='nw')
    b1.place(x=200,y=166,anchor='nw')
    b2.place(x=18,y=166,anchor='nw')
    top.mainloop()


root=Tk()
root.title("登陆界面")
root.resizable(False, False)
root.geometry("310x210")
l1=Label(root,text="登陆",font=("consolas","30",'bold italic'))
z1=Label(root)
l2=Label(root,text="用户名:",height=1,width=7)
l3=Label(root,text="密码:",height=1,width=7)
e1=Entry(root)
e2=Entry(root,show="*")
b1=Button(root,text="登陆",command=denglu,width=15,height=3)
b2=Button(root,text="注册",command=zhuce,width=15,height=3)
l1.pack()
l2.place(x=57, y=48, anchor='nw')
e1.place(x=109, y=48, anchor='nw')
l3.place(x=60, y=90, anchor='nw')
e2.place(x=109, y=90, anchor='nw')
b1.place(x=18, y=135, anchor='nw')
b2.place(x=178, y=135, anchor='nw')
print(b1.bind)
root.mainloop()
