import random as r
import math as m
g=0
b=0

for x in range(1000):
    #i=int(input("input:"))
    i=r.randint(1,1000)
    print("input="+str(i))
    x=1000
    k=0
    while m.floor(x)!=i:
        if x>i:
            x=x-(x/2)
            k=k+1
            #print(str(k)+"/"+str(x))
        elif x<i:
            x=x+(x/2)
            k=k+1
            #print(str(k)+"/"+str(x))
    print("Done,turn="+str(k))
    if k>i:
        b=b+1
    elif k<i:
        g=g+1
if b>g:
    print("bad!")
elif b==g:
    print("average")
else:
    print("good")
print(str(g)+"/"+str(b))
