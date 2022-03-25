while True:#here we made infinite amount of loop cuz it's every time would be true
    ssup = input ("how many cantimeters do ya have?  ")#made variable which we inputing
    try:#tryied to make commands if failed goes to except
        sup = float(ssup)#new variable that changing type of input to float
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
        print("ne nayebesh ne projivesh, poprobuy vvesti chislo - pidr")#if the code breaks we print this
