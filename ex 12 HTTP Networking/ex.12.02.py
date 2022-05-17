# Exercise 2: Change your socket program so that it counts the number of characters it has received and stops
# displaying any text after it has shown 3000 characters. The program should retrieve the entire document and
# count the total number of characters and display the count of the number of characters at the end of the document.
# urllib library in python that does all the socket work for us and makes web pages looks like a file
# http://www.py4inf.com/code/mbox-short.txt
import urllib.request
import urllib.parse
inp_adress = input("Type URL you need to connect to: ")
fhand = urllib.request.urlopen(inp_adress)
counts = dict()
counts_char = dict()
counts_word = 0
text = ""
try:
    for line in fhand:
        words = line.decode().split()
        line = line.decode().rstrip()
        text = text+line
        counts_word = counts_word+len(words)-1
        for word in words:
            characters = word
            counts[word] = counts.get(word, 0) + 1
            for character in characters:
                counts_char[character] = counts_char.get(character, 0)+1
except:
    print("ended")
# print(counts,"\n", counts_char,"\n", counts_word)
# print(text, len(text))
print(counts_char)
print(text[:3000], "\n amount of characters - ", len(text))
