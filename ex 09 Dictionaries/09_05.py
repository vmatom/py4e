#Exercise 5: This program records the domain name (instead of
#the address) where the message was sent from instead of who
#the mail came from (i.e., the whole email address). At the
#end of the program, print out the contents of your dictionary.
op=open(input("Ener a file name: "))
count=dict()
for line in op:
    line = line.rstrip()
    if not line.startswith('From ') :continue#cut all lines without FROM as started
    words = line.split() #split lanes as words
    words = words[1].split('@')
    words=words[1] #we need only 3rd word in the lane
    count[words]=count.get(words,0)+1 #we add to dictionary word and the count
print(count)
bigcount= None
bigword = None
for wrd, cnt in count.items():
    if bigcount is None or cnt > bigcount:
        bigword = wrd
        bigcount = cnt
print (bigword, bigcount)
print(count['gmail.com'])
