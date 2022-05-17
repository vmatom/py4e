# Exercise 2: Change your socket program so that it counts the number of characters it has received and stops
# displaying any text after it has shown 3000 characters. The program should retrieve the entire document and
# count the total number of characters and display the count of the number of characters at the end of the document.
# urllib library in python that does all the socket work for us and makes web pages looks like a file
# http://www.py4inf.com/code/mbox-short.txt
import urllib.request, urllib.error, urllib.parse
inpadr = input("Type URL you need to connect to: ")
fhand= urllib.request.urlopen(inpadr)
counts=dict()
countschar = dict()
countsword=0
text=""
try:
    for line in fhand:
        words =line.decode().split()
        line=line.decode().rstrip()
        text=text+line
        countsword=countsword+len(words)-1
        for word in words:
            characters = word
            counts[word] = counts.get(word, 0) + 1
            for character in characters:
                countschar[character] = countschar.get(character, 0)+1
except:
    print("ended")
# print(counts,"\n", countschar,"\n", countsword)
# print(text, len(text))
print(countschar)
print(text[:3000], "\n ammount of characters - ", len(text))
