#!/usr/bin/python3

def Fac():
    num = 5
    fac = 1
    while num > 0:
        fac *= num
        num -= 1
    return fac
result = Fac()
print(result)

import math
def fact(num):
    r = math.factorial(num)
    return r
result2 = fact(5)
print(result2)
