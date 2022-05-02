__all__=["Variable"]
class Variable(list):
    def __init__(self, *args):
        list.__init__([])
        self.extend([*args])

    def __add__(self, otro):
        if isinstance(otro, (int, float)):
            c = tuple(map(lambda a: a + otro, self))
        elif isinstance(otro, Variable):
            c = tuple(map(lambda a, b: a + b, self, otro))
        return Variable(*c)

    def __radd__(self, otro):
        if isinstance(otro, (int, float)):
            c = tuple(map(lambda a: otro + a, self))
        elif isinstance(otro, Variable):
            c = tuple(map(lambda a, b: b + a, self, otro))
        return Variable(*c)

    def __sub__(self, otro):
        if isinstance(otro, (int, float)):
            c = tuple(map(lambda a: a - otro, self))
        elif isinstance(otro, Variable):
            c = tuple(map(lambda a, b: a - b, self, otro))
        return Variable(*c)

    def __rsub__(self, otro):
        if isinstance(otro, (int, float)):
            c = tuple(map(lambda a: otro - a, self))
        elif isinstance(otro, Variable):
            c = tuple(map(lambda a, b: b - a, self, otro))
        return Variable(*c)

    def __mul__(self, otro):
        if isinstance(otro, (int, float)):
            c = tuple(map(lambda a: a * otro, self))
        elif isinstance(otro, Variable):
            c = tuple(map(lambda a, b: a * b, self, otro))
        return Variable(*c)

    def __rmul__(self, otro):
        if isinstance(otro, (int, float)):
            c = tuple(map(lambda a: otro * a, self))
        elif isinstance(otro, Variable):
            c = tuple(map(lambda a, b: b * a, self, otro))
        return Variable(*c)

    def __truediv__(self, otro):
        if isinstance(otro, (int, float)):
            c = tuple(map(lambda a: a / otro, self))
        elif isinstance(otro, Variable):
            c = tuple(map(lambda a, b: a / b, self, otro))
        return Variable(*c)

    def __rtruediv__(self, otro):
        if isinstance(otro, (int, float)):
            c = tuple(map(lambda a: otro, self))
        elif isinstance(otro, Variable):
            c = tuple(map(lambda a, b: b / a, self, otro))
        return Variable(*c)

    def __floordiv__(self, otro):
        if isinstance(otro, (int, float)):
            c = tuple(map(lambda a: a // otro, self))
        elif isinstance(otro, Variable):
            c = tuple(map(lambda a, b: a // b, self, otro))
        return Variable(*c)

    def __rfloordiv__(self, otro):
        if isinstance(otro, (int, float)):
            c = tuple(map(lambda a: otro // a, self))
        elif isinstance(otro, Variable):
            c = tuple(map(lambda a, b: b // a, self, otro))
        return Variable(*c)

    def __pow__(self, otro):
        if isinstance(otro, (int, float)):
            c = tuple(map(lambda a: a ** otro, self))
        elif isinstance(otro, Variable):
            c = tuple(map(lambda a, b: a ** b, self, otro))
        return Variable(*c)

    def __rpow__(self, otro):
        if isinstance(otro, (int, float)):
            c = tuple(map(lambda a: otro**a, self))
        elif isinstance(otro, Variable):
            c = tuple(map(lambda a, b: b**a, self, otro))
        return Variable(*c)

    def __round__(self, ndigits=0):
        c = tuple(map(lambda a: round(a, ndigits), self))
        return Variable(*c)

    def __abs__(self):
        c = tuple(map(lambda a: abs(a), self))
        return Variable(*c)

    def __int__(self):
        c = tuple(map(lambda a: int(a), self))
        return Variable(*c)

    def __float__(self):
        c = tuple(map(lambda a: float(a), self))
        return Variable(*c)

    def __neg__(self):
        c = tuple(map(lambda a: -a, self))
        return Variable(*c)

    def __pos__(self):
        c = tuple(map(lambda a: +a, self))
        return Variable(*c)
