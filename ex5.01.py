count = 0
tot = 0.0
par="Done"
while True:#start loop
    azura= input("Enter a number, when you done type 'Done' ")
#if azura is "Done" we breaking this loop and go to print ("Dis done")
    if azura == "Done":
        break
#after we understood azura type of azura we need to try to make azura as float
    try:
        fazura = float(azura)
#if we have some type of error we make except thing and make continue (back to 5th row)
    except:
        print ("Invalid input")
        continue
#every time we have all circumstances done we starting counting and make total
    count=count+1
    tot = tot+fazura
#this starts after BREAK on the 8th row. We end this program by printing
print ("Dis done")
print(tot, count, tot/count)
