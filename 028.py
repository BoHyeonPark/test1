#!/usr/bin/python3
seq1 = "ATGTTATAG"

new_seq = ""
for i in seq1:
    if i == "A":
        new_seq += "T"
    elif i == "T":
        new_seq += "A"
    elif i == "C":
        new_seq += "G"
    elif i == "G":
        new_seq += "C"
print(new_seq)

