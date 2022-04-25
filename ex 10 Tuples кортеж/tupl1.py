#tuples are immutable - кортежи неизменны. U can't modify tuples
#list is d = [1,2,3,4,5]
#d[2]=6 =>  d=[1,2,6,4,5]
#tuple is d = (1,2,3,4,5)
#d[2]=6 => object tuple does not support item Assignment
#u can't sort, append and reverse tuple either
#tuple are mor efficient, higher performance, lower memory usage
l = list()
print(dir(l))
t = tuple()
print(dir(t))
(a,b,c,)= ("arrow","bird",3)
print(a)
print(b)
print(c)

d = dict()
d['a']=10
d['b']=1
d['c']=22
for (k,v) in d.items():
    print(k,v)
    tups=d.items() #there would be 3 tuples ('a', 10) and ('b', 1) and ('c', 22)
    #dict_items([('a', 10), ('b', 1), ('c', 22)])
print(tups)
print(sorted(d.items())) #we sort it by 1st part of each tuples (a,b,c)
