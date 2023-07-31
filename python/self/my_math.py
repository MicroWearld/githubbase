from random import random,randint
from pylab import *

def build_line(X,k,ex):
	Y=list(map(lambda x:k*x+(-1)**randint(0,1)*random()*ex,X))
	return Y

def S2(X):
	x_=mean(X)
	s2=sum(list(map(lambda xi:(xi-x_)**2,X)))/len(X)
	return s2

def r(X,Y):
	x_,y_=mean(X),mean(Y)
	fz=sum(list(map(lambda xi,yi:(xi-x_)*(yi-y_),X,Y)))
	r=fz/(len(X)*S2(X)**0.5*S2(Y)**0.5)
	return r

def mean(X):
	mean=sum(X)/len(X)
	return mean

def linea_b(X,Y):
	x_=mean(X);y_=mean(Y)
	fz=sum(list(map(lambda xi,yi:(xi-x_)*(yi-y_),X,Y)))
	b=fz/(len(X)*S2(X))
	a=mean(Y)-b*mean(X)
	return a,b

def R2(X,Y):
	a,b=linea_b(X,Y)
	y_=mean(Y)
	Y1=list(map(lambda Xi:b*Xi+a,X))
	fz=sum(list(map(lambda Yi,Y1i:(Yi-Y1i)**2,Y,Y1)))
	fm=sum(list(map(lambda Yi:(Yi-y_)**2,Y)))
	R2=1-fz/fm
	return R2

def line_info(X,Y):
	X_=mean(X);Y_=mean(Y)
	SX2=S2(X);SY2=S2(Y)
	RXY=r(X,Y)
	r2=R2(X,Y)
	A,B=linea_b(X,Y)
	infol=["x_","y_","Sx2","Sy2","r","R2"]
	info=[X_,X_,SX2,SY2,RXY,r2]
	print("-"*20)
	print("info for the line:")
	for i in range(len(infol)):
		print(infol[i]+"="+str(info[i]))
	print("\nend")
	print("-"*20)

x=list(range(50))
y=build_line(x,2,10)
x+=[50];y+=[1000]
print(len(x),len(y))
sx2=S2(x);sy2=S2(y)
a,b=linea_b(x,y)
y1=list(map(lambda xi:b*xi+a,x))
line_info(x,y)
#-----------------------------------------------------------------------
xlim(-5,len(x)+5);ylim(min(y)-10,max(y)+10)
scatter(x,y,marker=".",label=f"data")
plot(x,y1,c="orange",label=f"line")
title("y=bx+a+e")
legend()
show()