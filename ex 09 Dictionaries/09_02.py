op=open(input("say the name of the file "))
count=dict()
#https://www.py4e.com/html3/09-dictionaries доделать все что ниже
for line in op:
    line = line.rstrip()
    if not line.startswith('From ') :continue#cut all lines without FROM as started
    words = line.split() #split lanes as words
    words=words[2] #we need only 3rd word in the lane
    count[words]=count.get(words,0)+1 #we add to dictionary word and the count
print(count)
