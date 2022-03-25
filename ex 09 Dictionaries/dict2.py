abc = dict()
abc['AAA']=1
abc['BBB']=1
print (abc)
abc['AAA']=abc['AAA']+1
abc['BBB']=abc['BBB']+1
print (abc)
count=dict()
names=['aaa','bbb','ccc','ddd','eee','aaa','ccc','aaa','aaa','ddd']
for name in names:
    if name not in count:
        count[name]=1
    else :
        count[name]=count[name]+1
print(count)

count2=dict()
names2=['aaa','bbb','ccc','ddd','eee','aaa','ccc','aaa','aaa','ddd']
for name in names2:
    count2[name]=count2.get(name, 0)+1#if we found in "names2" something that not
# in count2, we add it to the dictionary (count2), value for this index = 0+1
# if names2 in count2, we add 1 to value of this index
print(count2)
print(count2.get('aaa',2))
