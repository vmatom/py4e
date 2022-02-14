va = "Paritor moet ramu"
le = len(va)
fi = va.find("mo")
print (fi)#this is the number of the fi letters
va.startswith("Paritor")#check if va starts from thing in hook (True)
va.startswith("paritor")#check if va starts from thing in hook (False)
rep = va.replace("Paritor", "Papa")#we changing part ov va 1st part in hook and changin by 2nd part of hook
greet = "   Hello bob   "
greet.lstrip()#remove space in the left side
greet.rstrip()#remove space in the right side
greet.strip()#remove all spaces
print(rep)
print (le)
print(va[2:5])#not include 5
print(va[0:3])#not include 3
print(va[:10])#from 1st to the 9th
count = 1
while count<le:
    print (count, va[count-1])
    count=count+1
che = input("say to me letters ")
if che in va: #check if CHE is exist in VA
    print ("Found it!!")
else:
    print ("There is no letters like this")
miniva= va.lower() #made VA in small symbols
print (miniva)
if che<"moet":
    print ("nu-nu")
elif che>"moet":
    print ("okaaay")
