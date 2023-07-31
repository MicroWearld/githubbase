fare = True  # 平局判断
n = 5  # 成立数


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
    # 连线检测(方法:按方向取出数字相加,除以检测数(n),若等于第一个取出的数,则连线成功)
    global fare
    f, k = True, 0

    for y in range(len(sq)):  # 横向
        for x in range(len(sq[0])-n):
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
            fare = False
    return f
