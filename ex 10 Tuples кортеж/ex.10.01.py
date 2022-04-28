#Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and
#pull out the addresses from the line. Count the number of messages from each person
#using a dictionary.

#After all the data has been read, print the person with the most commits by
#creating a list of (count, email) tuples from the dictionary.
#Then sort the list in reverse order and print out the person who has the most commits.
op=open(input("Ener a file name: "))
count=dict()
for line in op:
    line = line.rstrip()
    if not line.startswith('From ') :continue#cut all lines without FROM as started
    words = line.split() #split lanes as words
    words=words[1] #we need only 3rd word in the lane
    count[words]=count.get(words,0)+1 #we add to dictionary word and the count

t=list()
for wrd, cnt in count.items():
    newt=(wrd,cnt)
    t.append(newt)
print("tuple:", t)
t=sorted(t,reverse=True)
print("tuple reverse:", t[:1])
