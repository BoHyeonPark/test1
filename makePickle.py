#!/usr/bin/python3
import pickle

with open("data.pickle",'wb') as fw:
    with open("test.tsv",'r') as fr:
        for line in fr:
            l = line.strip().split("\t")
            if l[2] == "Herpes":
                pickle.dump(l,fw)

