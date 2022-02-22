finame = input("say the name of file ")
if finame == "Prank":
    print("You have been punk'd!")
    quit
else:
    try:
        fhan = open (finame)
    except:
        print("Error, wrong file name ")
        quit #this needs to cancel this programm due error
    for line in fhan:
        mline=line.rstrip()
        print(mline.upper())
