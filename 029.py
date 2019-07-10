#!/usr/bin/python3
seq1 = "ATGTTATAG"
print("C" in seq1)

for s in seq1:
    b = (s == "C") #s == "C" -> False
    print(s,b)
    if b:
        break
import re
p = re.compile("C")
m = p.match(seq1)
print(m)
