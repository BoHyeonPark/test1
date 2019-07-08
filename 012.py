#!/usr/bin/python3

def Fac(num):
    fac = 1
    while num > 0:
        fac *= num
        num -= 1
    return fac
a = 3
result = Fac(a)
print(result)
