numb="Abc"
include=[]
while numb != "Done":
    numb=(input("Say the number: "))
    if numb.isdigit():
        include.append(int(numb))
    elif numb != "Done":
        print("not a number")
    else:
        break
mid_list=[]
def middle(t,k):
    k.append(t[0])
    k.append(t[-1])
middle(include,mid_list)
print(mid_list)
print("maximum: ", max(include))
print("minimum: ", min(include))
print(include)
def chop(t):
    del t[0]
    del t[-1]
chop(include)
print(include)
