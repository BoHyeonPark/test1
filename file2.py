#!/usr/bin/python3
with open("test.csv",'r') as fr:
    header = fr.readline().strip().split(",")
#    print(",".join(header))
    for line in fr:
        l = line.strip().split(",")
        id_ = l[0]
        seq = l[1]
        species = l[2]
        if species == "Herpes":
            print(line.strip())


