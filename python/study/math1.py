a=int(input("ENTER:"))
b=int(input("ENTER:"))
c=int(input("ENTER:"))
i=1

while i<=10000000:
    if (a%i==0 and b%i==0 and c%i==0):
        print(i)
    i+=1
