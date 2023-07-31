from random import randint
sq = [[0 for i in range(8)] for j in range(8)]
# 棋盘数组
zz0, zz1, zz2, zz3, zz4, zz5, zz6, zz7 = 0, 0, 0, 0, 0, 0, 0, 0  # 重力效果指针
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
                print(" ", end=" ")
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
            if sq[y][x] == sum(sq[y][x:x+4])/n and not(0 in sq[y][x:x+n]):
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

    global j, zz0, zz1, zz2, zz3, zz4, zz5, zz6, zz7
    while check(sq) and q:
        printf(sq)
        # return 0   #debug
        if j % 2 == 0:
            c = 1  # 玩家1
        else:
            c = 2  # 玩家2
        if c == 1:
            g = str(randint(1, 8))
            print("请一号玩家落子(列数):", g)
        else:
            g = str(randint(1, 8))
            print("请二号玩家落子(列数):", g)
        if g == '1':
            if zz0 == len(sq[0]):
                print("空间已满,无法落子!\n\n")
                continue
            else:
                sq[0][zz0] = c
                zz0 += 1
        elif g == '2':
            if zz1 == len(sq[0]):
                print("空间已满,无法落子!\n\n")
                continue
            else:
                sq[1][zz1] = c
                zz1 += 1
        elif g == '3':
            if zz2 == len(sq[0]):
                print("空间已满,无法落子!\n\n")
                continue
            else:
                sq[2][zz2] = c
                zz2 += 1
        elif g == '4':
            if zz3 == len(sq[0]):
                print("空间已满,无法落子!\n\n")
                continue
            else:
                sq[3][zz3] = c
                zz3 += 1
        elif g == '5':
            if zz4 == len(sq[0]):
                print("空间已满,无法落子!\n\n")
                continue
            else:
                sq[4][zz4] = c
                zz4 += 1
        elif g == '6':
            if zz5 == len(sq[0]):
                print("空间已满,无法落子!\n\n")
                continue
            else:
                sq[5][zz5] = c
                zz5 += 1
        elif g == '7':
            if zz6 == len(sq[0]):
                print("空间已满,无法落子!\n\n")
                continue
            else:
                sq[6][zz6] = c
                zz6 += 1
        elif g == '8':
            if zz7 == len(sq[0]):
                print("空间已满,无法落子!\n\n")
                continue
            else:
                sq[7][zz7] = c
                zz7 += 1
        elif g == "q":  # 强制退出
            return 0
        else:
            print("列数错误!\n\n")
            continue
        j += 1
        print("\n")
    printf(sq)
    if j % 2 == 0 and q:
        print("玩家二获胜!")
    elif j % 2 == 1 and q:
        print("玩家一获胜!")
    else:
        print("平局!")


main()
