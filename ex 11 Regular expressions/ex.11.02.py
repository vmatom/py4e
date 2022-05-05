#Exercise 2: Write a program to look for lines of the form:
#New Revision: 39772
#Extract the number from each of the lines using a regular
#expression and the findall() method. Compute the average
#of the numbers and print out the average as an integer.
import re
fname = input ("Enter file:")
hand = open (fname)
numlist=list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall("^New Revision: ([0-9.]+)", line)
    if len(stuff)!=1: continue
    num=int(stuff[0])
    numlist.append(num)
aver=int(sum(numlist)/len(numlist))
print(aver)
