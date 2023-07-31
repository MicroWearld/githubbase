twl = r'''0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm&#@$%^!*()_+-=[]{}\|:;"',<.>?/~` §'''
wlt = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
       'Q': 10, 'W': 11, 'E': 12, 'R': 13, 'T': 14, 'Y': 15, 'U': 16, 'I': 17, 'O': 18,
       'P': 19, 'A': 20, 'S': 21, 'D': 22, 'F': 23, 'G': 24, 'H': 25, 'J': 26, 'K': 27,
       'L': 28, 'Z': 29, 'X': 30, 'C': 31, 'V': 32, 'B': 33, 'N': 34, 'M': 35, 'q': 36,
       'w': 37, 'e': 38, 'r': 39, 't': 40, 'y': 41, 'u': 42, 'i': 43, 'o': 44, 'p': 45,
       'a': 46, 's': 47, 'd': 48, 'f': 49, 'g': 50, 'h': 51, 'j': 52, 'k': 53, 'l': 54,
       'z': 55, 'x': 56, 'c': 57, 'v': 58, 'b': 59, 'n': 60, 'm': 61, '&': 62, '#': 63,
       '@': 64, '$': 65, '%': 66, '^': 67, '!': 68, '*': 69, '(': 70, ')': 71, '_': 72,
       '+': 73, '-': 74, '=': 75, '[': 76, ']': 77, '{': 78, '}': 79, '\\': 80, '|': 81,
       ':': 82, ';': 83, '"': 84, "'": 85, ',': 86, '<': 87, '.': 88, '>': 89, '?': 90,
       '/': 91, '~': 92, '`': 93, " ": 94, "§": 95}

count = 6


def change(c):
    cp, ccp = [], []
    pc, y = 0, ""
    i = len(c) % count
    if i != 0:
        c = (count - i) * "0" + c
    j = len(c) // count
    for k in range(j):
        cp.append(c[k * count:k * count + count])
    for l in cp:
        ccp.append(bin2int(l))
    for m in ccp:
        y += twl[m]
    return y


def rchange(c):
    x = ""
    for i in c:
        c = wlt[i]
        c = int2bin(c)
        x += c
    return x


def bin2int(binx):
    intx = 0
    binx = binx[::-1]
    for i in range(len(binx)):
        if binx[i] == "1":
            intx += 2**i
    return intx


def int2bin(intx):
    p = ""
    if intx == 0:
        p = "00000"
        return p
    while intx != 0:
        n = str(intx % 2)
        intx = intx // 2
        p = n + p
    if len(p) % count != 0:
        p = "0" * (count - len(p) % count) + p
    return p
