finame = input("say the name of file ")
count=0
if finame == "Prank":
    print("You have been punk'd!")
    quit
else:
    try:
        fhan = open (finame)
        for line in fhan:
            if line.startswith ("Subject:"):
                count=count+1
        print("There were ", count, " subject lines in", finame)
    except:
        print("Error, wrong file name ")
        quit #this needs to cancel this programm due error
