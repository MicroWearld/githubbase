#python D:\IT\python\tester.py
from decimal import *
d=Decimal(input("Decimal:"))
N=0
while True:
	if 2**52<=(2**N)*d<2**53:
		break
	else:
		N+=1
q,r=divmod(2**N,1/d)
if r>5:
	q+=1
print("float:",format(q/2**N,".50f"))
print("N:",N)
print("q:",q)
print("r:",r)
print("d:",d)
