numb="Abc"
include=[]
while numb != "Done":
    numb=(input("Say the number: "))
    if numb =="Done":
        print("maximum: ", max(include))
        print("minimum: ", min(include))
        break
    else:
        try:
            numb=int(numb)
            include.append(numb)
        except:
            print("not a number")
