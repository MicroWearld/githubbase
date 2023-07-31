import os
sq = [[0 for i in range(8)] for j in range(8)]
# 棋盘数组
zz = [0, 0, 0, 0, 0, 0, 0, 0]  # 重力效果指针数组
j, q = 0, True  # 玩家切换数字,平局判断
n = 4  # 成立数


def printf(sq):  # 界面输出
    for i in range(len(sq[0])-1, -1, -1):
        for j in range(len(sq)):
            if sq[j][i] == 1:
                print("x", end=" ")
            elif sq[j][i] == 2:
                print("o", end=" ")
            else:
                print(".", end=" ")
        print("\n", end="")
    print("-"*(len(sq)*2-1))
    for i in range(len(sq)-1):
        print(i+1, end=" ")
    print(i+2)


def cay(sq, a, b):  # 纵向读取
    k = 0
    for i in range(n):
        if sq[b+i][a] == 0:
            k = -1
            break
        else:
            k += sq[b+i][a]
    return k


def cacro(sq, a, b):  # 斜向读取
    k, x, y = 0, 0, 0
    for i in range(n):
        if sq[a+y][b+x] == 0:
            k = -1
            break
        else:
            k += sq[a+y][b+x]
            x += 1
            y += 1
    return k


def carcro(sq, a, b):  # 反斜向读取
    k, x, y = 0, 0, 0
    for i in range(n):
        if sq[a+y][b+x] == 0:
            k = -1
            break
        else:
            k += sq[a+y][b+x]
            x -= 1
            y += 1
    return k


def check(sq):
    # 连线检测(方法:按方向取出数字相加,除以检测数(4),若等于第一个取出的数,则连线成功)
    global q
    f, k = True, 0

    for y in range(len(sq)):  # 横向
        for x in range(5):
            if sq[y][x] == sum(sq[y][x:x+n])/n and not(0 in sq[y][x:x+n]):
                f = False

    for y in range(len(sq[0])-n+1):  # 纵向
        for x in range(len(sq)):
            if sq[y][x] == cay(sq, x, y)/n:
                f = False

    for y in range(len(sq[0])-n+1):  # 斜向
        for x in range(len(sq[0])-n+1):
            if sq[y][x] == cacro(sq, y, x)/n:
                f = False

    for y in range(len(sq)-n+1):  # 反斜向
        for x in range(n-1, len(sq[0])):
            if sq[y][x] == carcro(sq, y, x)/n:
                f = False

    if f:
        for y in range(len(sq)):  # 平局
            for x in range(len(sq[0])):
                if sq[y][x] != 0:
                    k += 1
        if k == len(sq)*len(sq[0]):
            q = False
    return f


def main():  # 主体，玩家输入操作
    print('''四子棋游戏
规则:双方轮流下子(会受重力影响),当其中一方四子连成一线时,这一方获胜
强制退出:q''')

    global j
    while check(sq) and q:
        printf(sq)
        # return 0    #debug
        if j % 2 == 0:
            g = input("请一号玩家落子(列数):")
        else:
            g = input("请二号玩家落子(列数):")
        if not g.isdigit():
            if g == "q":
                print("强(你)制(玩)退(不)出(起)!")
                return "QUIT"
            else:
                os.system("cls")
                print("无效输入!\n")
                continue
        g = int(g)
        if g < 0 or g > len(sq):
            os.system("cls")
            print("位置错误!\n")
            continue
        if zz[g-1] == len(sq[0]):
            os.system("cls")
            print("空间已满,无法落子!\n")
            continue
        sq[g-1][zz[g-1]] = j % 2+1
        zz[g-1] += 1
        os.system("cls")
        j += 1
    printf(sq)
    if j % 2 == 0 and q:
        print("玩家二获胜!")
    elif j % 2 == 1 and q:
        print("玩家一获胜!")
    else:
        print("平局!")


main()
