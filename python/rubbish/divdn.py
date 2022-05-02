def divd(st):#分割函数，用"/"分割出分子和分母
    f,s,i="","",0
    flag=False
    if "/" in st:
        while i<=len(st)-1:
            if st[i]=="/":
                flag=True
                i+=1
            if flag:
                s+=st[i]
            else:
                f+=st[i]
            i+=1
    else:
        f,s=st,"1"
    return f,s
	
__f1,__f2,__f3,__s1,__s2,__s3=0,0,0,0,0,0

def check(f,s):#分数格式化(约分和化整)
    f,s=int(f),int(s)
    k,i=0,2
    if abs(f)<abs(s):
        k=abs(s)
    else:
        k=abs(f)
    while i<=k:
        if f%i==0 and s%i==0:
            f,s=f/i,s/i
        else:
            i+=1
    if abs(f)!=abs(s):
        if f<0 and s<0:
            f,s=abs(f),abs(s)
        elif f>0 and s<0:
            f,s=0-f,abs(s)
    else:
        if s<0 or f<0:
            st="-1"
        else:
            st="1"
    if f==0 and s!=0:
        st="0"
    elif f!=0 and s==1:
        st=str(int(f))
    elif s==0:
        st="错误!分母为零!"
    else:
        f,s=str(int(f)),str(int(s))
        st=f+"/"+s
    return st

def ftod(st):#浮点分数转分数
    f,s=divd(st)
    st1,st2,st3="","",""
    if "." in f:
        k,flag=0,False
        for i in range(len(f)-1):
            if f[i]==".":
                f=f.replace(".","")
                flag=True
            if flag:
                k+=1
        st1=f+"/"+str(10**k)
    else:
        st1=f
    if "." in s:
        k,flag=0,False
        for i in range(len(s)-1):
            if s[i]==".":
                s=s.replace(".","")
                flag=True
            if flag:
                k+=1
        st2=s+"/"+str(10**k)
    else:
        st2=s
    st3=div(st1,st2)
    return st3

def dtof(st):#分数转浮点数
    f,s=divd(st)
    f,s=float(f),float(s)
    return f/s

def plus(st1,st2):#加法函数
    global __f1,__f2,__f3,__s1,__s2,__s3
    __f1,__s1=divd(st1)
    __f2,__s2=divd(st2)
    __f1,__f2,__s1,__s2=int(__f1),int(__f2),int(__s1),int(__s2)
    __f3=__f1*__s2+__f2*__s1
    __s3=__s1*__s2
    return check(__f3,__s3)

def sub(st1,st2):#减法函数
    global __f1,__f2,__f3,__s1,__s2,__s3
    __f1,__s1=divd(st1)
    __f2,__s2=divd(st2)
    __f1,__f2,__s1,__s2=int(__f1),int(__f2),int(__s1),int(__s2)
    __f3=__f1*__s2-__f2*__s1
    __s3=__s1*__s2
    return check(__f3,__s3)

def muti(st1,st2):#乘法函数
    global __f1,__f2,__f3,__s1,__s2,__s3
    __f1,__s1=divd(st1)
    __f2,__s2=divd(st2)
    __f1,__f2,__s1,__s2=int(__f1),int(__f2),int(__s1),int(__s2)
    __f3=__f1*__f2
    __s3=__s1*__s2
    return check(__f3,__s3)

def div(st1,st2):#除法函数
    global __f1,__f2,__f3,__s1,__s2,__s3
    __f1,__s1=divd(st1)
    __f2,__s2=divd(st2)
    __f1,__f2,__s1,__s2=int(__f1),int(__f2),int(__s1),int(__s2)
    __f3=__f1*__s2
    __s3=__s1*__f2
    return check(__f3,__s3)

def compare(st1,cop,st2):#比较函数
    flag=False
    st3=sub(st1,st2)
    if cop=="==":
        if st3=="0":
            flag=True
    elif cop=="!=":
        if st3!="0":
            flag=True
    elif cop=="<":
        if "-" in st3:
            flag=True
    elif cop==">":
        if not("-" in st3):
            flag=True
    elif cop=="<=":
        if "-" in st3 or st3=="0":
            flag=True
    elif cop==">=":
        if not("-" in st3) or st3=="0":
            flag=True
    else:
        flag="NULL"
    return flag

#若要在python shell中使用,请将其复制到python主程序文件夹下的\Lib文件夹
#python D:\IT\python\self\divdn.py