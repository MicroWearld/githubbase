ant=[0,0,0,90]
alrd=[[0,0,0,90]]

def wind():
    if ant[2]==0:
        ant[3]=check(ant[3]+90)
    elif ant[2]==1:
        ant[3]=check(ant[3]-90)

def step():
    if ant[3]==0 or ant[3]==360:
        ant[0]=ant[0]+1
    elif ant[3]==90:
        ant[1]=ant[1]+1
    elif ant[3]==180:
        ant[0]=ant[0]-1
    elif ant[3]==270:
        ant[1]=ant[1]-1

def check(q):
    while q < 0 or q > 360:
        if q > 360:
            q -= 360
        elif q < 0:
            q += 360
    return q

def change():
    i=0
    while i<=len(alrd)-1:
        if ant[0]==alrd[i][0] and ant[1]==alrd[i][0]:
            if ant[2]==0:
                ant[2]=1
            else:
                ant[2]=0
            if alrd[i][2]==0:
                alrd[i][2]=1
            else:
                alrd[i][2]=0
        #print("loop on")
        i+=1

c=int(input("enter the step:"))
print("ant's possition:",ant)
for i in range(0,c,1):
    change()
    wind()
    step()
    print("step"+str(i+1)+":",ant)
    tmp=[ant[0],ant[1],ant[2]]
    alrd.append(tmp)
    change()
