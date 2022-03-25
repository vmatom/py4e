handle = open('mbox.txt', 'r')
#print(handle)
count=0
for read in handle:#(this is how we can read file in python)
    count =count+1
    #print (read)#it'd be a few lines READ became the last line
#print (read)
#print ("lines count is ",count)
fhan = open ('mbox-short.txt','r')
for line in fhan:
    line=line.rstrip()#we deleted the \n
    if line.startswith("From:"):
        print(line)
fhan = open ('mbox-short.txt','r')
for line in fhan:
    line=line.rstrip()#we deleted the \n
    if not line.startswith("From:"):#here we tryin to find NOT started by "From:"
#aaaand if it started like this we continueing print the lines
        continue
    print(line)
inp = fhan.read() #it's became 1 line without \n
#print (inp)
#schet = 'k&j\n=6'
#print (schet)
#len(schet)#length of \n is 1
