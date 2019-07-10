#!/usr/bin/python3
cnt = 0
snp_num = 0
ins_num = 0
del_num = 0
with open("070.vcf",'r') as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            l = line.split("\t")
            ref = l[3]
            alt = l[4].split(",")
            for a in alt:
                if len(ref) == len(a):
                    snp_num += 1
                elif len(ref) < len(a):
                    ins_num += 1
                elif len(ref) > len(a):
                    del_num += 1
print("snp:",snp_num)
print("ins:",ins_num)
print("del:",del_num)
