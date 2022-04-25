#Exercise 4: Add code to the above program to figure out who has
# the most messages in the file. After all the data has been read
#and the dictionary has been created, look through the dictionary
#using a maximum loop (see Chapter 5: Maximum and minimum loops)
#to find who has the most messages and print how many messages
#the person has.
op=open(input("Ener a file name: "))
count=dict()
for line in op:
    line = line.rstrip()
    if not line.startswith('From ') :continue#cut all lines without FROM as started
    words = line.split() #split lanes as words
    words=words[1] #we need only 3rd word in the lane
    count[words]=count.get(words,0)+1 #we add to dictionary word and the count
#print(count)
bigcount= None
bigword = None
for wrd, cnt in count.items():
    if bigcount is None or cnt > bigcount:
        bigword = wrd
        bigcount = cnt
print (bigword, bigcount)
