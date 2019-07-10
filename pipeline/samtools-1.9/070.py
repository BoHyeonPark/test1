#!/usr/bin/python3

cnt = 0
with open("070.vcf",'r') as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            cnt += 1
print(cnt)
