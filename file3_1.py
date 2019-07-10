#!/usr/bin/python3
import myModule

with open("test.tsv",'r') as fr:
    header = fr.readline().strip().split("\t")
#    print(",".join(header))
    for line in fr:
        l = line.strip().split("\t")
        id_ = l[0]
        seq = l[1]
        species = l[2]
        if species == "Herpes":
            gc = myModule.calcGC(seq)
            print(gc)
            print(line.strip())


