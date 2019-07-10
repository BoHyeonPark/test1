#!/usr/bin/python3
length = 0
with open("077.bed",'r') as fr:
    for line in fr:
        l = line.strip().split("\t")
        start = l[1]
        end = l[2]
        length += int(end) - int(start)
print(length)

