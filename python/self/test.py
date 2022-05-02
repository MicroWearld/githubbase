x=int(input("dgree:"))
while x<0 or x>360:
    if x>360:
        x-=360
    elif x<0:
        x+=360
print("result:",x)