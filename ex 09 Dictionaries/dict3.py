counts = dict() #create empty dictionary
line = input("Enter a line of the text\n") #enter the input information
disallowed_characters="!,.?:;'—.../n" #add line of punctuation marks that we need to expel
line = line.lower() #change all characters as lower case
for character in disallowed_characters:
    line = line.replace(character,'')#remove from input all punctuation marks
words= line.split() #split the input by words
print("Words are: ", words, "\nCounting...")
ammount=0
for word in words: #for every word in the "words" we do thing below
    counts[word] = counts.get(word,0) +1#we check 1st word if it is 1st time appear
    #we count it like 0 + 1, if it already existed - we add 1 more to it's count
    #get needed to get the value from of the word item
    ammount=ammount+1
#print('ammount of words is: ', ammount ,'counts - ', counts)
#for key, value in sorted(counts.items()):
    #print(key, " was found ", value, ' time(s).')
bigcount= None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print (bigword, bigcount)
