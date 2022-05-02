from change import change,rchange,wlt,twl
def search(st):
    global k
    if j%len(st)==0 and j!=0:
        k+=1
    return st[j-len(st)*k]

def locker(mingwen,miyao,mode):
    global j,k,de
    if mode=="encode":
        op=mingwen
        key=miyao
        j,k,check,sum=0,0,"",""
        for i in op:
            if i=="\n":
                continue
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
        return sum,key+"$"+change(check)
    elif mode=="decode":
        sum=mingwen
        yek=miyao
        yek=yek.split("$",1)
        check=rchange(yek[1])
        check=check[len(check)-len(sum):]
        yek=yek[0]
        j,k,num,op=0,0,0,""
        for i in range(len(sum)):
            if i=="\n":
                continue
            if check[i]=="0":
                num=0-wlt[sum[i]]
            else:
                num=wlt[sum[i]]
            rop=num+wlt[search(yek)]
            op=op+twl[rop]
            j+=1
        return op
