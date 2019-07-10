#!/usr/bin/python3
cnt = 0
with open("070.vcf",'r') as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            l = line.split("\t")
            if l[6] == "PASS":
                cnt += 1
print(cnt)
