han = open ('mbox-short.txt')
for line in han:
    line = line.rstrip()
    wds = line.split()
#guardian 1
    #if len(wds)<1:
        #continue #
#guardian 2
    #if line == '':
        #continue #
#guardian 3
    if not line.startswith("From"):
        continue #
#check for having From as 1st word in the line
    if wds[0] != 'From':
        continue
    print(wds[2])
