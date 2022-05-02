from tkinter import *
from change import change,rchange,wlt,twl
import tkinter.messagebox as tmb

def search(st):
    global k
    if j%len(st)==0 and j!=0:
        k+=1
    return st[j-len(st)*k]

def jiami(mingwen,miyao):
    global j,k,check
    op=mingwen
    key=miyao
    if op=="" or key=="":
        tmb.showerror(title="Error",message="options blank!")
        return None
    j,k,check,sums=0,0,"",""
    for i in op:
        num=wlt[i]-wlt[search(key)]
        if num<0:
            num=abs(num)
            check=check+"0"
            word=twl[num]
        else:
            check=check+"1"
            word=twl[num]
        sums=sums+word
        j+=1
    miwene.delete(1.0,END)
    gongyaoe.delete(1.0,END)
    miwene.insert(1.0,sums)
    gongyaoe.insert(1.0,f"{key}${change(check)}")

def jeimi(miwen,gongyao):
    global j,k,check
    sums=miwen
    yek=gongyao
    if sums=="" or yek=="":
        tmb.showerror(title="Error",message="options blank!")
        return None
    yek=yek.split("$",1)
    check=rchange(yek[1])
    check=check[len(check)-len(sums):]
    yek=yek[0]
    j,k,num,op=0,0,0,""
    for i in range(len(sums)):
        if check[i]=="0":
            num=0-wlt[sums[i]]
        else:
            num=wlt[sums[i]]
        rop=num+wlt[search(yek)]
        op=op+twl[rop]
        j+=1
    mingwene.delete(1.0,END)
    miyaoe.delete(1.0,END)
    mingwene.insert(1.0,op)
    miyaoe.insert(1.0,yek)

def clear():
    miwene.delete(1.0,END)
    gongyaoe.delete(1.0,END)
    mingwene.delete(1.0,END)
    miyaoe.delete(1.0,END)
    

root=Tk()
root.title("字符串加密/解密程序")
root.resizable(False, False)
root.geometry("625x415+400+150")
mingwen=Label(root,text="明文:")
mingwene=Text(root,width=40,height=10)
miyao=Label(root,text="私钥:")
miyaoe=Text(root,width=40,height=10)
miwen=Label(root,text="密文:")
miwene=Text(root,width=40,height=10)
gongyao=Label(root,text="公钥:")
gongyaoe=Text(root,width=40,height=10)
code=Button(root,text="加密",command=lambda:jiami(mingwene.get(1.0,END).replace("\n",""),miyaoe.get(1.0,END).replace("\n","")),height=1,width=30)
decode=Button(root,text="解密",command=lambda:jeimi(miwene.get(1.0,END).replace("\n",""),gongyaoe.get(1.0,END).replace("\n","")),height=1,width=30)
erase=Button(root,text="清除",command=clear)
mingwen.place(anchor="nw",x=10,y=10)
mingwene.place(anchor="nw",x=10,y=40)
miyao.place(anchor="nw",x=320,y=10)
miyaoe.place(anchor="nw",x=320,y=40)
miwen.place(anchor="nw",x=10,y=240)
miwene.place(anchor="nw",x=10,y=270)
gongyao.place(anchor="nw",x=320,y=240)
gongyaoe.place(anchor="nw",x=320,y=270)
code.place(anchor="nw",x=12,y=200)
decode.place(anchor="nw",x=385,y=200)
erase.place(anchor="nw",x=290,y=200)
root.mainloop()
