#!/usr/bin/python3
def calcGC(s):
    num_c = s.count("C")
    num_g = s.count("G")
    gc = float(num_c + num_g)/len(s) * 100
    return gc

if __name__ == "__main__":
    s = ""
    with open("sequence.txt",'r') as fr:
        for line in fr:
            s += line.strip()
    print(s)
    gc = calcGC(s)
    print(gc)

