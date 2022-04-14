phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
for i in range (4):
    plist.pop()
print(plist)
plist.remove("D")
print(plist)
plist.remove("'")
print(plist)#ont pa
plist.insert(2, plist.pop(3))
print(plist)#on tpa
plist.append(plist.pop(-2))
print(plist)
new_phrase=''.join(plist)
print(plist)
print(new_phrase)
