#!/usr/bin/python3
'''
write_string = "Hello\nhaha\nwowwow\n"

with open("write_sample.txt",'w') as fw:
    fw.write(write_string)
'''
with open("test.txt",'r') as fr:
    for line in fr:
        print(line.strip())
w_str = "Hello\nACGT\n12345\n"

with open("test.txt",'w') as fw:
    fw.write(w_str)

with open("test",'w') as fw:
    with open("test",'r') as fr:
        for line in fr:
#            fw.write(line)
            chr = line.split("\t")[0]
            pos = line.split("\t")[1]
            ref = line.split("\t")[3]
            alt = line.split("\t")[4]
            fw.write(chr+"\t"+pos+"\t"+ref+"\t"+alt+"\n")
