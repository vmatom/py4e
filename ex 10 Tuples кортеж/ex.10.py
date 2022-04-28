fname = input ('Enter the name of the file ')
if len(fname)<1 : fname = 'clown.txt'
hand = open (fname)
di=dict()
for lin in hand:
    lin=lin.rstrip()
    wds=lin.split()
    for w in wds:
    #    if w not in di:
    #        di[w]=1
    #    else:
    #        di[w]=di[w]+1
        #if the key is not here >> this counts as 0
        #oldcount = di.get(w,0)
        #newcount=oldcount+1
        #di[w]= newcount
        di[w]=di.get(w,0)+1 #idion: retrieve/create/update counter
#print(di)
tmp=list()
for k,v in di.items():
    newt=(v,k)
    tmp.append(newt)
print(tmp)
tmp= sorted (tmp,reverse=True)
print (tmp)
for v,k in tmp[:5]:
    print (k,v)


x= (di.items())
x= [(v,k) for k,v in di.items()]
x=sorted(x,reverse=True)
#print (x[:5])
for v,k in x[:5]:
    print (k,v)
