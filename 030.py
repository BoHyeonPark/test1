#!/usr/bin/python3
seq1 = "AGTTTATAG"
motif = "TT"
for i in range(len(seq1)):
    if seq1[i:i+len(motif)] == motif:
        print(i)

for i in range(len(seq1)):
    if seq1[i:i+2] == "TT":
        print(i, "-->", i, ":", i+2, seq1[i:i+2])

for i in range(0,len(seq1),1):
    print(i,i+2,seq1[i:i+2])
