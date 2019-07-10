#!/usr/bin/python3

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)
result = fac(5)
print(result)

'''
num = 5
fac = 1
while num > 0 :
    fac *= num
    num -= 1
print(fac)
'''

#fibonachii 0, 1, 1, 2, 3
import sys
n = sys.argv[1]
def f(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return f(n-2) + f(n-1)
p_result = f(n)
print(p_result)

for i in range(1,11,1):
    print(i, f(i))
'''
l = [0,1]
for i in range(10):
    val = l[-2] + l[-1]
    l.append((val)
print(l)
'''
