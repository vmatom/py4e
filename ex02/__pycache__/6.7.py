name = "Vladislav"
sname = "Mitrokhin"
x=0
frt = name[x], sname[x] #can't be more than ammount of letters
print (frt)#this is 1st letter of name and surname
le=len(name)#length
sle=len(sname)
print(le)
print(sle)
while x < le:
    frt = name[x],sname[x]
    print (frt,x)
    x=x+1
for frt in name:
    print (frt)
count=0
san = input("say the letter you wanna know ")
for letter in name:#"in" makes ORDER from left to right
    if letter == san:
        count=count+1
print("ammount of ", san," - ", count)
