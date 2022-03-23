fhand = open('mbox-short1.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From': continue
    if words[0] == 'From' and len(words)> 2:
         print(words[2])
