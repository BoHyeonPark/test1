#!/usr/bin/python3
l = [3,1,1,2,0,0,2,3,3]
print(max(l))
print(min(l))


for i in range(0,len(l),1):
    if i == 0: #set max_val, min_val
        max_val = l[i]
        min_val = l[i]
    else:
        if max_val < l[i]:
            max_val = l[i] #max_val change
        if min_val > l[i]:
            min_val = l[i] #min_val change
print("max:",max_val)
print("min:",min_val)
