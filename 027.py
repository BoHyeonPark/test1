#!/usr/bin/python3
seq1 = "ATGTTATAG"
print(seq1[::-1])

rev_seq1 = ""
for i in range(len(seq1)-1,-1,-1):
    rev_seq1 += seq1[i]
print(rev_seq1)
