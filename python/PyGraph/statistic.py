from random import random, randint, choice
from _frac_copy_adapted_version import Fraction, Decimal
import math
__all__ = ["build_line_data", "var", "mean", "line_ab",
           "sinfo", "cor", "cor2", "arrang", "combin",
           "Binary_Dist", "HyperGeometric_Dist", "B",
           "A", "C", "HG", "frac", "Fraction", "deci",
           "Decimal", "Normal_Dist", "N"]

__version__ = 1.0


def _prints(lis, row):
    if len(lis) % row == 0:
        r = len(lis) // row
    else:
        r = len(lis) // row + 1
    for i in range(r):
        for j in range(row):
            if i + j * r <= len(lis) - 1:
                print(lis[i + j * r], end="")
        print()


def build_line_data(X, k, ran, e):
    "Return a linear regression module."
    Y = []
    rand = [0] * int(ran * 100) + [1] * int(100 - ran * 100)
    for xi in X:
        f = choice(rand)
        yi = k * xi + (-1)**f * random() * e
        Y.append(yi)
    return Y


def var(X):
    "Return variance"
    SX2 = sum(list(map(lambda xi: (xi - mean(X))**2, X))) / len(X)
    return SX2


def cor(X, Y):
    "Return Correlation coefficient about two datas."
    fz = sum(list(map(lambda xi, yi: (xi - mean(X)) * (yi - mean(Y)), X, Y)))
    fm = len(X) * var(X)**0.5 * var(Y)**0.5
    r = fz / fm
    return r


def line_ab(X, Y):
    "Return linear regression index(a hat and b hat)."
    fz = sum(list(map(lambda xi, yi: (xi - mean(X)) * (yi - mean(Y)), X, Y)))
    fm = len(X) * var(X)
    b = fz / fm
    a = mean(Y) - b * mean(X)
    return a, b


def cor2(Y, Y1):
    "Return coefficient of determination about two modules."
    fz = sum(list(map(lambda yi, y1i: (yi - y1i)**2, Y, Y1)))
    fm = len(Y) * var(Y)
    r2 = 1 - fz / fm
    return r2


def mean(X):
    "Other name for average"
    mean = sum(X) / len(X)
    return mean


def arrang(fm, to):
    A = 1
    for a in range(fm, fm - to, -1):
        A *= a
    return A


def combin(fm, to):
    return int(arrang(fm, to) / arrang(to, to))


def percentage(X, ft=0.5):
    x = x.sort()
    i = len(x) * ft
    if isinstance(i, int):
        return mean([X[i], X[i + 1]])
    else:
        return X[int(i) + 1]


def Binary_Dist(n, p, rou=None):
    bd = {}
    for i in range(n + 1):
        if rou == None:
            bd[i] = combin(n, i) * (1 - p)**(n - i) * p**i
        else:
            bd[i] = round(combin(n, i) * (1 - p)**(n - i) * p**i, rou)
    return bd


def HyperGeometric_Dist(N, M, n, rou=None):
    hgd = {}
    for i in range(max([0, n - N + M]), min([n, M]) + 1):
        if rou == None:
            hgd[i] = combin(M, i) * combin(N - M, n - i) / combin(N, n)
        else:
            hgd[i] = round(combin(M, i) * combin(N - M,
                                                 n - i) / combin(N, n), rou)
    return hgd


def Normal_Dist(MIU, SIGMA, xrang, limx=0.0001):
    def f(x): return (1 / (SIGMA * (2 * math.pi)**0.5)) * \
        math.e**(-(x - MIU)**2 / (2 * SIGMA**2))

    if SIGMA <= 0:
        raise AttributeError("SIGMA can\'t be zero or negative number!")
    else:
        c, s = xrang[0], 0
        while c <= xrang[1]:
            r = f(c) * limx
            c += limx
            s += r
        return s


def sinfo(X, Y, s=True, column=5, standard=21, rou=2, ste=1):
    "Show statistics info and data."
    infol = []
    c = 0
    print("-" * 42)
    print("statistic info for X,Y:\n")
    if s:
        print("liner_index:")
        print("X_=" + str(mean(X)) + " , " + "Y_=" + str(mean(Y)))
        print("SX2=" + str(var(X)) + " , " + "SY2=" + str(var(Y)))
        print("r:", cor(X, Y))
        a, b = line_ab(X, Y)
        Y1 = list(map(lambda xi: b * xi + a, X))
        print("r2", cor2(Y, Y1))
        print("end_.\n")
    print("data:")
    for i in range(0, len(X), ste):
        infol.append("X=" + str(round(X[i], rou)) +
                     "->" + "Y=" + str(round(Y[i], rou)))
        c += 1
    infol = list(map(lambda i: i + (standard - len(i)) * " ", infol))
    _prints(infol, row)
    print(f"count of data on show:{c}")
    print(f"total count of data:{len(X)}")
    print("end_.\n")
    print("-" * 42)


def domain(start, end, step):
    "Set your 'x' from start to end,which setp is step(defination of domain)."
    lis = []
    c = start
    while c <= end:
        lis.append(c)
        c += step
    return lis


def integrate(f, bot, top, lim=0.00001):
    x = domain(bot, top, lim)
    x1, x2 = x[:-1], x[1:]
    y = list(map(lambda a, b: (b - a) * f((b + a) / 2), x1, x2))
    res = sum(y)
    return res


# Other name for functions:
A = arrang
C = combin
B = Binary_Dist
HG = HyperGeometric_Dist
frac = Fraction
deci = Decimal
N = Normal_Dist
