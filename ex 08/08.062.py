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
print("maximum: ", max(include))
print("minimum: ", min(include))
