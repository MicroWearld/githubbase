from divdn import *
de=0
def test():
    global de
    a=input("第一个分数或整数a:")
    b=input("第二个分数或整数b:")   
    c=input("输入关系运算符(可选):")
    d=input("输入一个带浮点数的分数c:")
    f=input("输入第四个分数d:")
    print(a,"+",b,"=",plus(ftod(a),ftod(b)))
    print(a,"-",b,"=",sub(ftod(a),ftod(b)))
    print(a,"*",b,"=",muti(ftod(a),ftod(b)))
    print(a,"/",b,"=",div(ftod(a),ftod(b)))
    print("c的化简结果:",ftod(d))
    print("d的小数结果:",dtof(f))
    if len(c)>0:
        print(a,c,b,"-->",compare(ftod(a),c,ftod(b)))
    if de==0:
        con=input("\n重试? Y=1;N=0:")
        if con=="1":
            print("-"*79)
            test()
        de=1

test() 
