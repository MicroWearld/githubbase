from random import random

s=float(input("请输入红包总金额:"))
n=int(input("请输入发放红包的个数:"))
l=[]
k=s
for i in range(1,n):
	d=s*random()
	s-=d
	l.append(d)
	print("第",i,"个红包:",d,"元")
print("第",n,"个红包:",k-sum(l),"元")
l.append(k-sum(l))
print("红包王是第",l.index(max(l))+1,"个红包,金额为",max(l),"元")
