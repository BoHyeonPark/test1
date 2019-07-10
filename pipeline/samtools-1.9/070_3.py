#!/usr/bin/python3
with open("070.vcf",'r') as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            l = line.split("\t")
            chrom = l[0]
            pos = l[1]
            rsid = l[2]
            ref = l[3]
            alt = l[4]

            if rsid != ".":
                print(chrom+"\t"+pos+"\t"+ref+"\t"+alt+"\t"+rsid)
