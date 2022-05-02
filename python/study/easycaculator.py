#python D:\IT\python\easycaculator.py
flag=0
fn=float(input("输入第一个数:"))
sy=input("输入运算符:")
sn=float(input("输入第二个数:"))
if sy=="+":
	re=fn+sn
elif sy=="-":
	re=fn-sn
elif sy=="*":
	re=fn*sn
elif sy=="/":
	if sy==0:
		flag=1
	else:
		re=fn/sn
else:
	flag=2
	print("错误!")
	
if flag==1:
	print("除数为零!")
elif flag==0:
	print(fn,sy,sn,"=",re)