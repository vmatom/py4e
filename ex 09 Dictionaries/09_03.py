#Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.
op=open(input("say the name of the file "))
count=dict()
for line in op:
    line = line.rstrip()
    if not line.startswith('From ') :continue#cut all lines without FROM as started
    words = line.split() #split lanes as words
    words=words[1] #we need only 3rd word in the lane
    count[words]=count.get(words,0)+1 #we add to dictionary word and the count
print(count)
