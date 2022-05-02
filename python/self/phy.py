L=[]
V=[]
a=0
i=0
t=float(input("input time:"))
while True:
    a=input("input length:")
    if a!="/":
        L.append(float(a))
    else:
        break

while i<=len(L)-2:
    V.append((0.01*(L[i]+L[i+1]))/(2*t))
    print("V"+str(i+2)+"=",V[i],end=" ")
    i+=1
    
