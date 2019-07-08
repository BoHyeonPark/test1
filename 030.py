#!/usr/bin/python3
seq1 = "AGTTTATAG"
motif = "TT"
for i in range(len(seq1)):
    if seq1[i:i+len(motif)] == motif:
        print(i)
