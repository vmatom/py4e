while True:
    def calculpay (Hour, Rate):
        # print ("Calculation started","ur hour is", Hour,"ur rate is", Rate)
        if (Hour >= 40):
            addpay = (Hour-40) * Rate*0.5#if hours per week more than 40 hours, we need to pay more. ammount of "more" is 50% of hours over the 40
        else:
            addpay = 0
        Pay = float(Hour)*float(Rate) + addpay #changing type of variable to float thing
        return Pay #here we just bring the Pay as a result of this def function
    try:
        HR = float(input ("Enter Hours  "))#enters hour
        RE = float(input("Enter Rate  "))#enters rate
        #FR = float(RE)#changing type of input from string to the floating
        #FH = float(HR) #changing type of input from string to the floating
        FP = calculpay(HR, RE) #we are using def function with 2 variables float hours and float rate. FP
        print("Your Pay is ", FP) #final thing
    except ValueError:
        print("wrong enter \ntry again")
print("wrong enter \ntry again", None)
a=None
b=4
if a<b:
    print ("dada")
else:
    print ("net net")
