frlist= set(["Mark", "Nark", "Shark"])#lists
lolist = set(["Coke", "White", "Socks", "Shark", "Mark"])#lists
nolist = "Can't change"#we can't change str in this case
print("length of nolist is", len(nolist))

print(lolist)
print(lolist-frlist)
list=lolist-frlist
a = set('qwerty')
b = frozenset('qwerty')
a == b
print (a)
a.add(1)
print (a)
