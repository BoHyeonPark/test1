#!/usr/bin/python3
cnt = 0
with open("070.vcf",'r') as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            l = line.split("\t")
            alt = l[4].split(",")
            for a in alt:
                cnt += 1
#                if "," not in alt:
#                    cnt += 1
print(cnt)
