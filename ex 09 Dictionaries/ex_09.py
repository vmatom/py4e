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
print(di)
bigword=None
bigcount=None
#assignment of word and count values by ".items()"
for word, count in di.items():
    if bigcount is None or count>bigcount:
        bigcount=count
        bigword=word
print(bigword,bigcount)
