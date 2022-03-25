loop = input ("Say me number ")
floop = float(loop)
while floop>=0: #small loop that would be if var more or equal zero
    print(floop)
    floop = floop - 1 #we changin the variable
print ("1st part", floop) #it say that 1st part is ended

#here started new part
while True:
    anvar = input ("> ")
    if anvar == "done":
        break
    print (anvar)
print ("this is good")
