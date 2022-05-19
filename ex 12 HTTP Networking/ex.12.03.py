# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL,
# (2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document.
# Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents.
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
        text += line
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
