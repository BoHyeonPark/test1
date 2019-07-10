#!/usr/bin/python3
import json

f = "test.json"

with open(f,'r') as fr:
    data = json.load(fr)
print(data)
print(type(data))
