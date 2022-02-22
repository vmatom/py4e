fhan = open ('mbox-short.txt','r')
for line in fhan:
    line=line.rstrip()#we deleted the \n
    if not "@uct.ac.za" in line :
        continue
    print(line)
inp = fhan.read() #it's became 1 line without \n
