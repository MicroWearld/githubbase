from random import randint
sq=[[0 for i in range(19)] for j in range(19)]
alpha={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
ahpla="abcdefghijklmnopqrstuvwxyz"
allow=[]
#棋盘数组
j,q=0,True    #玩家切换数字,平局判断
n=5    #成立数
def chachong(g,allow):
    while g in allow:
        g=ahpla[randint(1,18)]+str(randint(1,19))
    return g

def printf(sq):#界面输出
    for i in range(len(sq[0])-1,-1,-1):
        for j in range(len(sq)):
            if sq[j][i]==1:
                print("x",end=" ")
            elif sq[j][i]==2:
                print("o",end=" ")
            else:
                print(" ",end=" ")
        print(i+1,end="")
        print("\n",end="")
    for i in range(len(sq)-1):
        print(ahpla[i],end=" ")
    print(ahpla[i+1])

def sp(strg):
    strg1=[]
    strg1.append(alpha[strg[0]])
    if not strg[1:].isdigit():
        strg1.append("NULL")
    else:
        strg1.append(int(strg[1:])-1)
    return strg1

def cay(sq,a,b):#纵向读取
    k=0
    for i in range(n):
        if sq[b+i][a]==0:
            k=-1
            break;
        else:
            k+=sq[b+i][a]
    return k

def cacro(sq,a,b):#斜向读取
    k,x,y=0,0,0
    for i in range(n):
        if sq[a+y][b+x]==0:
            k=-1
            break;
        else:
            k+=sq[a+y][b+x]
            x+=1
            y+=1
    return k

def carcro(sq,a,b):#反斜向读取
    k,x,y=0,0,0
    for i in range(n):
        if sq[a+y][b+x]==0:
            k=-1
            break;
        else:
            k+=sq[a+y][b+x]
            x-=1
            y+=1
    return k

def check(sq):
#连线检测(方法:按方向取出数字相加,除以检测数(n),若等于第一个取出的数,则连线成功)
    global q
    f,k=True,0

    for y in range(len(sq)):#横向
        for x in range(len(sq[0])-n):
            if sq[y][x]==sum(sq[y][x:x+n])/n and not(0 in sq[y][x:x+n]):
                f=False

    for y in range(len(sq[0])-n):#纵向
        for x in range(len(sq)):
            if sq[y][x]==cay(sq,x,y)/n:
                f=False

    for y in range(len(sq[0])-n):#斜向
        for x in range(len(sq[0])-n):
            if sq[y][x]==cacro(sq,y,x)/n:
                f=False

    for y in range(len(sq)-n):#反斜向
        for x in range(n-1,len(sq[0])):
            if sq[y][x]==carcro(sq,y,x)/n:
                f=False

    if f:
        for y in range(len(sq)):#平局
            for x in range(len(sq[0])):
                if sq[y][x]!=0:
                    k+=1
        if k==len(sq)*len(sq[0]):
            q=False
    return f

def main():#主体，玩家输入操作
    global j
    print('''五子棋游戏''')
    while check(sq) and q:
        flag=True
        print(f"round:{j+1}")
        printf(sq)
        if j%2==0:
            print("\n\nx:一号/o:二号\n请一号玩家落子(行数【字母】列数【数字】):")
            g=chachong(ahpla[randint(1,18)]+str(randint(1,19)),allow)
            allow.append(g)
            ge=1
        else:
            print("\n\nx:一号/o:二号\n请一号玩家落子(行数【字母】列数【数字】):")
            g=chachong(ahpla[randint(1,18)]+str(randint(1,19)),allow)
            allow.append(g)
            ge=2
        if len(g)<=1 or g[0] not in ahpla:
            print("位置错误!\n\n\n\n")
            continue
        g=sp(g)
        if g[1]=="NULL" or g[1]>len(sq[0])-1:
            print("位置错误!\n\n\n\n")
            continue
        if sq[g[0]][g[1]]==0:
            sq[g[0]][g[1]]=ge
            j+=1
        elif sq[g[0]][g[1]]==1 or sq[g[0]][g[1]]==2:
            print("该位置已有棋子!\n\n\n\n")
    print(f"round:{j+1}")
    printf(sq)
    if j%2==0 and q:
        print("玩家二获胜!")
    elif j%2==1 and q:
        print("玩家一获胜!")
    else:
        print("平局!")
main()