fx="x**3"
x=1
def sigma(st,en):
    c=0
    for i in range(st,en+1):
        c+=(x/en)*((x-i*(x/en))**3)
    return c

print(sigma(1,2**100))
