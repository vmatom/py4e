d = {'a':10, 'b':1,'c':22}
t= sorted(d.items())
print(t)
#[('a', 10), ('b', 1), ('c', 22)]
for (k,v) in sorted(d.items()):
    print(k,v)
    #a 10
    #b 1
    #c 22

#SORT BY VALUE NOT THE KEY
c = {'a':10, 'b':1,'c':22}
tmp=list()
for (k,v) in c.items():
    tmp.append((v,k))#ATTENTION we change the order of k and v,
    #it needed to sort by values not keys
print (tmp)
tmp=sorted(tmp,reverse=True)
print (tmp)

#AND EQUAL THING IS

e = {'a':10, 'b':1,'c':22}
di=dict()
print (sorted([(v,k) for k,v in e.items()]))
di=sorted([(v,k) for k,v in e.items()])
print(di)
