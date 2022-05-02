from dn import dn
flag=0
fn=dn(input("输入第一个数:"))
sy=input("输入运算符:")
sn=dn(input("输入第二个数:"))
if sy=="+":
    re=fn+sn
elif sy=="-":
    re=fn-sn
elif sy=="*":
    re=fn*sn
elif sy=="/":
    if sy=="0":
	    flag=1
    else:
        re=fn/sn
elif sy=="**":
    re=fn**sn
else:
    flag=2
    print("错误!")
print(fn,sy,sn,"=",re)
