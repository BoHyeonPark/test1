#!/usr/bin/python3

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)
print(fac(5))


'''
num = 5
fac = 1
while num > 0 :
    fac *= num
    num -= 1
print(fac)
'''
