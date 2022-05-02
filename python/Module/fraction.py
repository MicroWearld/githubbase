import operator


class Fraction_ERROR(Exception):
    '''
    这是分数异常类
    定义分数异常Fraction_ERROR
    继承于”异常类“(Exception)
    在出现分数赋值错误时抛出该异常类型
    '''


class frac:  # 定义分数类
    "分数类,输入一个分数字符串"

    def __init__(self, dnstr):
        if "/" in dnstr:
            dnd = dnstr.split("/")
        else:
            dnd = [dnstr, "1"]
        if "." in dnstr:
            for j in range(2):
                if "." in dnd[j]:
                    k = 0
                    for i in dnd[j]:
                        if i == ".":
                            break
                        k += 1
                    k = len(dnd[j]) - k - 1
                    dnd[j] = (dnd[j].replace(".", "") + "/" + str(10**k))
                else:
                    dnd[j] = (dnd[j] + "/1")
            dnd = (dnd[0] + "/" + dnd[1]).split("/")
        self.f = dnd[0]  # 分子
        self.s = dnd[1]  # 分母
        if spellcheck(self.f, self.s)[2]:
            raise Fraction_ERROR(
                'You cannot use non numeric characters as numerators and denominators!')  # 异常抛出,下同
        if spellcheck(self.f, self.s)[0]:
            raise Fraction_ERROR(
                'You cannot use non numeric characters as numerators!')
        if spellcheck(self.f, self.s)[1]:
            raise Fraction_ERROR(
                'You cannot use non numeric characters as denominators!')
        if self.s == '0':
            raise Fraction_ERROR('You cannot use zero as denominators!')

    def __str__(self):
        return str(check(self.f, self.s))

    def __repr__(self):
        return str(check(self.f, self.s))

    def _operator_fallbacks(monomorphic_operator, fallback_operator):
        def forward(a, b):
            if isinstance(b, (int, frac)):
                return monomorphic_operator(a, b)
            elif isinstance(b, float):
                return fallback_operator(float(a), b)
            else:
                return NotImplemented
        forward.__name__ = '__' + fallback_operator.__name__ + '__'
        forward.__doc__ = monomorphic_operator.__doc__

        def reverse(b, a):
            if isinstance(a, int):
                # Includes ints.
                return monomorphic_operator(a, b)
            elif isinstance(a, float):
                return fallback_operator(float(a), float(b))
            else:
                return NotImplemented
        reverse.__name__ = '__r' + fallback_operator.__name__ + '__'
        reverse.__doc__ = monomorphic_operator.__doc__

        return forward, reverse

    def _add(self, otrd):  # 加法a+b
        if not isinstance(otrd, frac):
            otrd = frac(f"{otrd}")
        if not isinstance(self, frac):
            self = frac(f"{self}")
        f1 = int(self.f)
        s1 = int(self.s)
        f2 = int(otrd.f)
        s2 = int(otrd.s)
        f3 = f1 * s2 + s1 * f2
        s3 = s1 * s2
        return frac(check(f3, s3))

    __add__, __radd__ = _add, _add

    def _sub(self, otrd):  # 减法a-b
        if not isinstance(otrd, frac):
            otrd = frac(f"{otrd}")
        if not isinstance(self, frac):
            self = frac(f"{self}")
        f1 = int(self.f)
        s1 = int(self.s)
        f2 = int(otrd.f)
        s2 = int(otrd.s)
        f3 = f1 * s2 - s1 * f2
        s3 = s1 * s2
        return frac(check(f3, s3))

    __sub__, __rsub__ = _operator_fallbacks(_sub, operator.sub)

    def _mul(self, otrd):  # 乘法a*b
        if not isinstance(otrd, frac):
            otrd = frac(f"{otrd}")
        if not isinstance(self, frac):
            self = frac(f"{self}")
        f1 = int(self.f)
        s1 = int(self.s)
        f2 = int(otrd.f)
        s2 = int(otrd.s)
        f3 = f1 * f2
        s3 = s1 * s2
        return frac(check(f3, s3))

    __mul__, __rmul__ = _mul, _mul

    def _truediv(self, otrd):  # 除法a/b
        if not isinstance(otrd, frac):
            otrd = frac(f"{otrd}")
        if not isinstance(self, frac):
            self = frac(f"{self}")
        f1 = int(self.f)
        s1 = int(self.s)
        f2 = int(otrd.f)
        s2 = int(otrd.s)
        f3 = f1 * s2
        s3 = f2 * s1
        return frac(check(f3, s3))

    __truediv__, __rtruediv__ = _operator_fallbacks(_truediv, operator.truediv)

    def __pow__(self, otrd):  # 幂运算a**b(b为整数)
        f1 = int(self.f)
        s1 = int(self.s)
        f2 = int(otrd.f)
        s2 = int(otrd.s)
        f3 = (f1**f2)**(1 / s2)
        s3 = (s1**f2)**(1 / s2)
        print(f3, s3)
        return frac(check(f3, s3))

    def __neg__(self):  # 取负-a
        if "-" in self.f:
            f = self.f.replace("-", "")
        else:
            f = "-" + self.f
        return frac(check(f, self.s))

    def __abs__(self):  # 取绝对值abs(a)
        f = self.f
        s = self.s
        if "-" in self.f:
            f = self.f.replace("-", "")
        if "-" in self.s:
            s = self.s.replace("-", "")
        return frac(check(f, s))

    def __float__(self):  # 化为小数
        return float(self.f) / float(self.s)

    def __eq__(self, otrd):  # 相等比较a==b
        flag = False
        ch = subout(self, otrd)  # 调用辅助减法函数,下同
        if ch == "0":
            flag = True
        return flag

    def __ne__(self, otrd):  # 不等比较a!=b
        flag = False
        ch = subout(self, otrd)
        if ch != "0":
            flag = True
        return flag

    def __gt__(self, otrd):  # 大于比较a>b
        flag = False
        ch = subout(self, otrd)
        if '-' not in ch:
            flag = True
        return flag

    def __ge__(self, otrd):  # 大于等于比较a>=b
        flag = False
        ch = subout(self, otrd)
        if '-' not in ch or ch == "0":
            flag = True
        return flag

    def __lt__(self, otrd):  # 小于比较a<b
        flag = False
        ch = subout(self, otrd)
        if '-' in ch:
            flag = True
        return flag

    def __le__(self, otrd):  # 小于等于比较a>=b
        flag = False
        ch = subout(self, otrd)
        if '-' in ch or ch == "0":
            flag = True
        return flag


def check(f, s):  # 分数格式化(约分和化整)
    f, s = int(f), int(s)
    k, i = 0, 2
    if abs(f) < abs(s):
        k = abs(s)
    else:
        k = abs(f)
    while i <= k:
        if f % i == 0 and s % i == 0:
            f, s = f / i, s / i
        else:
            i += 1
    if abs(f) != abs(s):
        if f < 0 and s < 0:
            f, s = abs(f), abs(s)
        elif f > 0 and s < 0:
            f, s = 0 - f, abs(s)
    else:
        if s < 0 or f < 0:
            st = '-1'
        else:
            st = '1'
    if f == 0 and s != 0:
        st = "0"
    elif f != 0 and s == 1:
        st = str(int(f))
    elif s == 0:
        raise ZeroDivisionError('Divisor is 0!')
    else:
        f, s = str(int(f)), str(int(s))
        st = f + "/" + s
    return st


def subout(a, b):  # 辅助减法,用于比较运算,请勿使用在实际程序中!
    f1 = int(a.f)
    s1 = int(a.s)
    f2 = int(b.f)
    s2 = int(b.s)
    f3 = f1 * s2 - s1 * f2
    s3 = s1 * s2
    return check(f3, s3)


def spellcheck(dnd1, dnd2):  # 分数合法检查,请勿使用在实际程序中!
    allow1 = "-+"  # 分子和分母开头中允许出现的字符
    allow2 = "0123456789."  # 分子和分母中允许出现的字符
    k, j = 0, 0
    check = [False for i in range(3)]
    if dnd1[0] in allow1:
        k = 1
    if dnd2[0] in allow1:
        j = 1
    for st in dnd1:
        for ts in st[k:]:
            if ts not in allow2:
                check[0] = True
                break
    for st in dnd2:
        for ts in st[j:]:
            if ts not in allow2:
                check[1] = True
                break
    if check[0] and check[1]:
        check[2] = True
    return check

# 以下为测试代码----------------------------------------------------------------------


def test():  # 测试函数
    "Quick test."
    a = frac(input("a="))
    b = frac(input("b="))
    print("\n----------RESULT----------")
    print(a, "+", b, "=", a + b)
    print(a, "-", b, "=", a - b)
    print(a, "*", b, "=", a * b)
    print(a, "/", b, "=", a / b)
    print(a, "**", b, "=", a**b)
    print("-a =", -a)
    print("-b =", -b)
    print("abs(a) =", abs(a))
    print("abs(b) =", abs(b))
    print("float(a) =", float(a))
    print("float(b) =", float(b))


__all__ = ["frac", "test"]
__version__ = 1.0
