#!/usr/bin/python3
try:
    with open("noname.txt",'r') as fr:
        read = fr.readlines()
    print(read)
except FileNotFoundError:
    print("file is not found")
