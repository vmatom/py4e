#Exercise 3: Write a program that reads a file and prints the letters in
#decreasing order of frequency. Your program should convert all the input
#to lower case and only count the letters a-z. Your program should not count
#spaces, digits, punctuation, or anything other than the letters a-z.
#Find text samples from several different languages and see how letter
#frequency varies between languages. Compare your results with the tables
#at https://wikipedia.org/wiki/Letter_frequencies.
counts = dict() #create empty dictionary
disallowed_characters="!,.?:;'—...\n1234567890()-/+><#@$%^&*~№| " #add line of punctuation marks that we need to expel
try:
    op = open(input("Enter a file name:")).read().lower()
except FileNotFoundError:
    print('File cannot be opened:', fname)
    quit()
for character in disallowed_characters:
    op= op.replace(character,'')
#print(op)
#type(op)
letters=list()
#print(letters)
for i in op:
    counts[i]=counts.get(i,0)+1
#print(counts)
for k,v in counts.items():
    letters.append((v,k))
letters=sorted(letters,reverse=True)
for v,k in letters:
    print (k,v)
