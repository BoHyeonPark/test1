#!/usr/bin/python3
import sys
'''
if len(sys.argv) != 2:
    print("#usage: python %s " % sys.argv[1])
    sys.exit()
'''
def kmer(base1,base2,num):
    if num == 1:
        return base2

    base_tmp = [] #new result
    for s1 in base1:
        for s2 in base2:
            base_tmp.append(s1+s2)
    return kmer(base1, base_tmp, num-1)

if __name__ == "__main__":
    num = int(sys.argv[1])
    base1 = ["A","C","G","T"] #template
    base2 = ["A","C","G","T"] #result

    result = kmer(base1,base2,num)
    print(result)
'''
cnt = 0
for i in range(len(result)):
    for j in 
    if result[0] == base2[-1] and base2[1] == base2[-2] and base2[2] == base[-3]:
        cnt += 1
print(cnt)

'''
