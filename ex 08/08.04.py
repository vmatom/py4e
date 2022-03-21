uni_text = open ('romeo.txt')
words = uni_text.read()
words = words.lower()
words=words.split()
unique = []
for word in words:
    if not word in unique:
        unique.append(word)
print (unique)
unique.sort()
print (unique)
