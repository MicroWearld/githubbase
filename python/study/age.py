f=open("a.txt","r",encoding="utf8")
l=f.readline().strip()
n=[]
while l!="":
	k=l.split(" ")
	n.append(int(k[1]))
	l=f.readline().strip()
print("老师年龄列表为:",n)
print("最大年龄为",max(n),"岁,最小年龄为",min(n),"岁,平均年龄为",sum(n)/len(n),"岁")