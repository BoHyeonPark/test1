#!/usr/bin/python3

seq = ""
d = {}
lineNum = 0
with open("061.fastq",'r') as fr:
    for line in fr:
        if lineNum % 4 == 0: #header
            pass
        elif lineNum % 4 == 1: #seq
            seq += line.strip()
        elif lineNum % 4 == 2: #+
            pass
        elif lineNum % 4 == 3: #qual
            pass

        lineNum += 1

        for i in seq:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
print("num of reads:",lineNum/4)
print("length of seq:",len(seq))
print(d)
