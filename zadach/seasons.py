def season(ugh):
    if ugh == 12 or ugh == 1 or ugh ==2:
        print("Winter tho")
    elif ugh >= 3 and ugh <=5:
        print("Spring babe ")
    elif ugh >= 6 and ugh <=8:
        print("Summer set ")
    elif ugh >= 9 and ugh <=11:
        print("Summer set ")
    else:
        print("This is not number of the month")
try:
    ugh=int(input("choose number of month between 1-12   -   "))
    se=season(ugh)

except:
    print ("this is not number tho")
