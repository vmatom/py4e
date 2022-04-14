phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
plist=plist[1:8:]#['o', 'n', "'", 't', ' ', 'p', 'a']
new_phrase="".join(plist[0:2])
print(new_phrase)
new_phrase=new_phrase+"".join(plist[4:2:-1])
print(new_phrase)
new_phrase=new_phrase+"".join([plist[-1],plist[-2]])
print(new_phrase)
print(plist)

#for i in range (4):
#    plist.pop()
#print(plist)
#plist.remove("D")
#print(plist)
#plist.remove("'")
#print(plist)#ont pa
#plist.insert(2, plist.pop(3))
#print(plist)#on tpa
#plist.append(plist.pop(-2))
#print(plist)
#new_phrase=''.join(plist)
