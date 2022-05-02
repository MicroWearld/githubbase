#python D:\IT\python\fl.py
tz=float(input("输入投资金额:"))
mz=float(input("输入目标金额:"))
sy=float(input("输入年利率(%):"))
i=0
fl=tz
while fl<mz:
	fl=fl*(1+sy/100)
	i+=1
	print("第"+str(i)+"年的年末本息为:"+str(fl))
print("达到目标收益金额需要"+str(i)+"年")