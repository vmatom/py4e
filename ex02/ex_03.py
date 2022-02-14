def insstr():#making function called insstr
    return "papamoetramu"#this function changing insstr to thing in ""
def bibka(skill):#in the () is the variable and we after can use it, you can use multiply variables in ()
    if skill == "pro":
        return "gg"
    elif skill == "average":
        return "luck"
    else:
        return "bg"

hour = input ("Enter Hours  ")#enters hour
Rate = input ("Enter Rate  ")#enters rate

Pay = float(hour)*float(Rate) #changing type of variable to float thing

print("Your Pay is ", Pay) #final thing
print("Your ", insstr())
print(15/100)
print (bibka("eq"))
def multyply(a,b,c,d):
    res = a*b*c*d
    return res
a = int(input ("say me a"))
b = int(input ("say me b"))
c = int(input ("say me c"))
d = int(input ("say me d"))

e = multyply(a,b,c,d)
print(e)
