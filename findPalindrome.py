#!/usr/bin/python3
import sys
import kmer

def checkPalindrome(s):
    s_rev = s[::-1]
    if s == s_rev:
        return True
    else:
        return False

if len(sys.argv) != 2:
    print("#usage: python %s [number]" % sys.argv[0])
    sys.exit()

num = int(sys.argv[1])
base1 = ["A","C","G","T"]
base2 = ["A","C","G","T"]
result = assignment2_6.kmer(base1,base2,num)

cnt = 0
for mer in result:
    if checkPalindrome(mer):
        cnt += 1
print(cnt)





