from random import random,randint,choice
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

def _prints(lis,row):
    if len(lis)%row==0:
        r=len(lis)//row
    else:
        r=len(lis)//row+1
    for i in range(r):
        for j in range(row):
            if i+j*r<=len(lis)-1:
                print(lis[i+j*r],end="")
        print()

def build_line_data(X,k,ran,e):
    Y=[]
    rand=[0]*int(ran*100)+[1]*int(100-ran*100)
    for xi in X:
        f=choice(rand)
        yi=k*xi+(-1)**f*random()*e
        Y.append(yi)
    return Y

def s2(X):
    SX2=sum(list(map(lambda xi:(xi-mean(X))**2,X)))/len(X)
    return SX2

def r(X,Y):
    fz=sum(list(map(lambda xi,yi:(xi-mean(X))*(yi-mean(Y)),X,Y)))
    fm=len(X)*s2(X)**0.5*s2(Y)**0.5
    r=fz/fm
    return r

def line_ab(X,Y):
    fz=sum(list(map(lambda xi,yi:(xi-mean(X))*(yi-mean(Y)),X,Y)))
    fm=len(X)*s2(X)
    b=fz/fm
    a=mean(Y)-b*mean(X)
    return a,b

def r2(Y,Y1):
    fz=sum(list(map(lambda yi,y1i:(yi-y1i)**2,Y,Y1)))
    fm=len(Y)*s2(Y)
    r2=1-fz/fm
    return r2

def mean(X):
    mean=sum(X)/len(X)
    return mean

def sinfo(X,Y,row=5,standard=21,rou=2):
    infol=[]
    print("-"*42)
    print("statistic info for X,Y:\n")
    print("index:")
    print("X_="+str(mean(X))+" | "+"Y_="+str(mean(Y)))
    print("SX2="+str(s2(X))+" | "+"SY2="+str(s2(Y)))
    print("r:",r(X,Y))
    a,b=line_ab(X,Y)
    Y1=list(map(lambda xi:b*xi+a,X))
    print("r2",r2(Y,Y1))
    print("end_.\n")
    print("data:")
    for i in range(len(X)):
        infol.append("X="+str(round(X[i],rou))+"->"+"Y="+str(round(Y[i],rou)))
    infol=list(map(lambda i:i+(standard-len(i))*" ",infol))
    _prints(infol,row)
    print("end_.\n")
    print("-"*42)
