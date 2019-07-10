#!/usr/bin/python3
'''
seq = ""
with open("059.fasta",'r') as fr:
    for line in fr:
        if line.startswith(">"):
            pass
        else:
            seq += line.strip()
print(len(seq))
'''
def fastaToString(f):
    seq = ""
    with open(f,'r') as fr:
        for line in fr:
            if line.startswith(">"):
                pass
            else:
                seq += line.strip()
    return seq

f = "059.fasta"
seq = fastaToString(f)
print(len(seq))
print("A", seq.count("A"))
print("T", seq.count("T"))
print("G", seq.count("G"))
print("C", seq.count("C"))
