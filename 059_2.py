#!/usr/bin/python3

d = {}
with open("059.fasta",'r') as fr:
    for line in fr:
        if line.startswith(">"):
            pass
        else:
            for i in line.strip():
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
print(d)
