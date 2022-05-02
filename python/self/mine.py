from random import randint

field=[[[".","."] for a in range(5)] for b in range(5)]
n=1
for i in field:
    print(n,end="|")
    n+=1
    for j in i:
        print(j[0],end=" ")
    print()
print(" ",end="")
for i in range(5):
    print(" "+str(i),end="")
