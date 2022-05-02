from change import change,rchange,wlt,twl
def search(st):
    global k
    if j%len(st)==0 and j!=0:
        k+=1
    return st[j-len(st)*k]

def main():
    print("-"*50)
    global j,k,de
    print("公私钥加密程序v0.1\n")
    print("选项:\n1.加密 2.解密 3.退出")
    mode=input("请选择:")
    print("-"*21)
    if mode=="1":
        op=input("输入明文:")
        key=input("输入私钥:")
        j,k,check,sum=0,0,"",""
        for i in op:
            num=wlt[i]-wlt[search(key)]
            if num<0:
                num=abs(num)
                check=check+"0"
                word=twl[num]
            else:
                check=check+"1"
                word=twl[num]
            sum=sum+word
            j+=1
        print("密文:"+sum)
        print("公钥:"+key+"$"+change(check))
        print("请保管好密文和公钥，否则将无法正确解密!")
        main()
    elif mode=="2":
        sum=input("输入密文:")
        yek=input("输入公钥:")
        yek=yek.split("$",1)
        check=rchange(yek[1])
        check=check[len(check)-len(sum):]
        yek=yek[0]
        j,k,num,op=0,0,0,""
        for i in range(len(sum)):
            if check[i]=="0":
                num=0-wlt[sum[i]]
            else:
                num=wlt[sum[i]]
            rop=num+wlt[search(yek)]
            op=op+twl[rop]
            j+=1
        print("明文:"+op)
        main()
    else:
        return None
main()
