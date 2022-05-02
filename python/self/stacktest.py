a=[]
zza=-1
for i in range(10):
	b=int(input("enter:"))
	a.append(b)
	zza+=1
print(a)
for x in range(10):
	p=a.pop(zza)
	print(a,p)
	zza-=1
