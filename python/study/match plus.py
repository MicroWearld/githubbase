s=input("输入数字:")
y=len(s)
sum=0
m={0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
for x in range(y):
    a=int(s[x])
    sum=sum+m[a]
print("需火柴数:",sum)
    
