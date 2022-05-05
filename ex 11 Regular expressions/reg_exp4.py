import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    print(type(num))
    numlist.append(num)
print("Maximum:", max(numlist))
#if we need to find special character - we need to use \
import re
x = "We just received $10.00 for cookies."
y = re.findall('\$[0-9.]+',x)
print (y)
