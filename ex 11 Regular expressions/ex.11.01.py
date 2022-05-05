#Exercise 1: Write a simple program to simulate the operation of the grep
#command on Unix. Ask the user to enter a regular expression and count
#the number of lines that matched the regular expression:
import re
user = str(input ('Enter a regular expression: '))
fname = "mbox.txt"
hand = open (fname)
print(user)
ammount=0
for line in hand:
    line = line.rstrip()
    stuff = re.findall(user, line)
    if len(stuff)!=1: continue
    ammount= ammount+1
    stuff= stuff[0]
print(fname, " had ", ammount, " lines that matched ", user)
