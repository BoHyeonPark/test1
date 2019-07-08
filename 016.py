#!/usr/bin/python3
fr = open("test.txt",'r')
lines = fr.readlines()
for line in lines:
    line = line.strip()
    print(line)
fr.close()

with open("test.txt",'r') as fr:
    for line in fr:
        print (line.strip())
