def insstr():
    print("papamoetramu")
while True:
    ssup = input ("how many cantimeters do ya have?  ")
    try:#tryied to make commands if failed goes to excep
        sup = float(ssup)#change type of input
        strong = sup+sup/6#add variable strong which uses
        if (sup>18): #findin out range of sup
            print("hello liar","it would reduce till ",strong/10)
        elif (12<=sup<=18):
            print("hello middle one:)","it'd grow till ",strong)
        elif (9<sup<12):
            print("Asian?","it'd grow till ",strong)
        elif (0<sup<=9):
            print("hello lil boiii","it'd grow till ",strong)
        else:
            print("It is vagina! ")

    except:#if goes wrong in begining >>> it's goes here
        print("ne nayebesh ne projivesh, poprobuy vvesti chislo - pidr")
print(15/100)
#auto-py-to-exe - to make exe from PY file
