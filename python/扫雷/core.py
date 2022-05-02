import tkinter.messagebox as tmb
from time import time
from tkinter import Button,Label,Menu,Widget,Tk,PhotoImage
from functools import partial
from random import randint
from locker import locker

colnum=[None,"blue","green","red","purple","orange","cyan","brown","black"]

def addc(bsq,pos:list):
    i,j=pos
    count=0
    for a in [i-1,i,i+1]:
        for b in [j-1,j,j+1]:
            count+=bsq[a][b].mine
    return count

def addm(bsq,pos:list):
    i,j=pos
    count=0
    for a in [i-1,i,i+1]:
        for b in [j-1,j,j+1]:
            if bsq[a][b].flag==1:
                count+=1
    return count

def cheat(bsq):
    for line in range(1,len(bsq)-1):
        for ll in range(1,len(bsq[0])-1):
            print(bsq[line][ll].mine,end=" ")
        print()

def setmine(bsq,num):
    for cho in range(num):
        r,c=randint(1,len(bsq)-2),randint(1,len(bsq[0])-2)
        while bsq[r][c].mine==1:
            r,c=randint(1,len(bsq)-2),randint(1,len(bsq[0])-2)
        bsq[r][c].mine=1
    for i in (0,len(bsq)-1):
        for j in (1,len(bsq[0])-1):
            bsq[i][j].cm=False

def showmine(bsq):
    for i in range(1,len(bsq)-1):
        for j in range(1,len(bsq[0])-1):
            if bsq[i][j].mine==1:
                if bsq[i][j].flag==1:
                    bsq[i][j]["text"]="%X"
                elif bsq[i][j].flag==2:
                    bsq[i][j]["text"]="?X"
                else:
                    bsq[i][j]["text"]="X"

def B_lock(bsq):
    for i in bsq:
        for j in i:
            if j.cm:
                j["state"]="disabled"
            j.unbind("<3>")
            j.unbind("<Double-Button-1>")
            j.flag=0

def tB_lock(bsq):
    for i in bsq:
        for j in i:
            if j.cm:
                j["state"]="disabled"
            j.unbind("<3>")
            j.unbind("<Double-Button-1>")

def author():
    tmb.showinfo(title="hi",message="程序设计:Diode_VD\n算法提供:City")

def rrecord():
    f=open("score.score","r")
    reed=list(map(lambda s:s.replace("\n",""),f.readlines()))
    oosre=reed[0].split(",")
    osre=[]
    for sre in range(len(oosre)):
        osre.append(float(locker(oosre[sre],reed[sre+1],"decode")))
    f.close()
    return osre

def wrecord(dif,score):
    s="";keys=""
    ds={"easy":0,"normal":1,"hard":2}
    sd=["easy","normal","hard"]
    osre=rrecord()
    osre[ds[dif]]=score
    for i in range(len(osre)):
        s+=(locker(str(osre[i]),sd[i],"encode")[0]+",")
        keys+=(locker(str(osre[i]),sd[i],"encode")[1]+"\n")
    f=open("score.score","w")
    f.write(s[:len(s)-1]+"\n"+keys)
    f.close()

def countt(c):
    if c==float("inf"):
        return "尚无记录"
    m=int(c//60)
    s=round(c%60,2)
    return f"{m}'{s}\""

def checksc(num,score):
    sear={10:0,40:1,99:2}
    ds={10:"easy",40:"normal",99:"hard"}
    if float(rrecord()[sear[num]])>score:
        tmb.showinfo(title="新纪录!",message=f'''最高记录:{countt(float(rrecord()[sear[num]]))}\n此次记录:{countt(score)}\n恭喜打破记录!''')
        wrecord(ds[num],score)

def allblank(bsq,num):
    stt=0
    for i in range(1,len(bsq)-1):
        for j in range(1,len(bsq[0])-1):
            if bsq[i][j].cm or bsq[i][j].mine==1:
                stt+=1
    if stt==num:
        return True
    return False

def rollmine(bsq,pos):
    bsq[pos[0]][pos[1]].mine=0
    r,c=randint(1,len(bsq)-2),randint(1,len(bsq[0])-2)
    while bsq[r][c].mine==1 or (r==pos[0] and c==pos[1]):
        r,c=randint(1,len(bsq)-2),randint(1,len(bsq[0])-2)
    bsq[r][c].mine=1

def showrecord():
    R=list(map(float,rrecord()))
    e,n,h=list(map(lambda r:countt(r),R))
    tmb.showinfo(title="记录",message=f"简单:{e}\n普通:{n}\n困难:{h}")

def tut():
    tmb.showinfo(title="按键说明",message="左键:排雷"+" "*15+"右键:标旗\n\nr键:新游戏"+" "*15+"q键:退出\n\n双击左键:拓展已知雷区\n\n注:所有字母均为小写,请勿打开大写锁定!")

def kill(Tk):
    Tk.destroy()
