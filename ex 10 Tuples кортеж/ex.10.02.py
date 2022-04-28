#Exercise 2: This program counts the distribution of the hour of the day for
#each of the messages. You can pull the hour from the “From” line by finding
#the time string and then splitting that string into parts using the colon
#character. Once you have accumulated the counts for each hour, print out
#the counts, one per line, sorted by hour as shown below.
try:
    op=open(input("Ener a file name: "))
except FileNotFoundError:
    print('File cannot be opened:', fname)
    quit()
#C:\Users\Professional\Desktop\py4e\ex 10 Tuples кортеж\mbox-short.txt
count=dict()
t=list()
for line in op:
    line = line.rstrip()
    if not line.startswith('From ') :continue#cut all lines without FROM as started
    words = line.split() #split lanes as words
#['From', 'rjlowe@iupui.edu', 'Fri', 'Jan', '4', '14:50:18', '2008']
    words=words[5]
    #14:50:18
    words = words.split(":")
    words=words[0]
    count[words]=count.get(words,0)+1 #we add to dictionary word and the count
for wrd, cnt in count.items():
    tup= (wrd,cnt)
    t.append(tup)
t=sorted(t)
#print (*t, sep="\n")
#for i in t:
#    print (i)
for key,value in t:
    print (key, value)
    #for w,c in t.items():
#    print(w,c)
