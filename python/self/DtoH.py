while True:
    d=input("RGB:")
    d=map(int,d.split(","))
    r=16
    re="#"
    H="abcdef"
    for i in d:
        s=""
        while i>0:
            i,n=divmod(i,r)
            if 10<=n<=15:
                n=H[n-10]
            s=str(n)+s
        re=re+s
    print("result:",re)