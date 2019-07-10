#!/usr/bin/python3
seq1 = "ATGTTATAG"
new_seq = ""
seq_dic = {"A":"T","T":"A","C":"G","G":"C"}
for i in seq1:
    new_seq += seq_dic[i]
print(seq1)
print(new_seq)


new_seq1 = ""
for i in seq1:
    if i == "A":
        new_seq1 += "T"
    elif i == "T":
        new_seq1 += "A"
    elif i == "C":
        new_seq1 += "G"
    elif i == "G":
        new_seq1 += "C"
print(seq1)
print(new_seq1)

