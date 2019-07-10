#!/usr/bin/python3
import sys
num = int(sys.argv[1])

def kmer(base1,base2,num):
    if num == 1:
        return base2

    base_tmp = [] #new result
    for s1 in base1:
        for s2 in base2:
            base_tmp.append(s1+s2)
    return kmer(base1, base_tmp, num-1)

base1 = ["A","C","G","T"] #template
base2 = ["A","C","G","T"] #result

result = kmer(base1,base2,num)
print(result)
'''
b = ["A","C","G","T"]
b2 = []
b3 = []
for i in b:
    for ii in b:
        b2.append(i+ii)
for j in b2:
    for jj in b:
        b3.append(j+jj)
print(b3)
'''
