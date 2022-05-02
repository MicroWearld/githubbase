print("1.milk[count:3;price:8]\n2.drink[count:5;price:6]\n3.water[count:2;price:5]\n")
while True:
    a=int(input("id:"))
    ct=["null",3,5,2]
    pc=["null",8,6,5]
    if a>3 or a<=0:
        print("error,try again!\n")
    else:
        b=int(input("count:"))
        if b>ct[a] or b<=0:
            print("error,try again!\n")
        else:
            c=int(input("price:"))
            if c<b*pc[a]:
                print("error,try again!\n")
            else:
                c=c-b*pc[a]
                print("right,",c)
                break
