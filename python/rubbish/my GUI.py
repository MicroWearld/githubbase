from tkinter import *
import tkinter.messagebox

a,i=0,0
def pen():
   import turtle
   n=int(E1.get())
   a=float(E2.get())
   d=(n-2)*180/n
   t=turtle.Pen()
   for i in range(n):
       t.forward(a)
       t.left(180-d)
   turtle.done()

def mess():
   while True:
      tkinter.messagebox.showerror(title='0xc00000001', message='Your PC ran into a problem \n Please restart your PC')
   
top=Tk()
top.title("turtle GUI By:王辰宇")
top.resizable(False,False)
top.geometry("300x150")
L1=Label(top,text="欢迎使用turtle GUI")
E1=Entry(top)
E2=Entry(top)
B1=Button(top,text ="绘制",width=12,height=1,command=pen)
B2=Button(top,text="Don`t touch it",width=12,height=1,command=mess)
L1.pack(),E1.pack(),E2.pack(),B1.pack(),B2.pack()
top.mainloop()

