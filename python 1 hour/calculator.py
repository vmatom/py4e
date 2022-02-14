# just try to make calculator
while True:
    try:
        ffrt = float(input ("1st number "))
        fscd = float(input ("2nd number "))
        oper = input ("what you want to do? +,-,/,*,^,%    ")
        if oper == "+":
            res=ffrt+fscd
        elif oper == "-":
            res=ffrt-fscd
        elif oper == "/":
            res=ffrt/fscd
        elif oper == "*":
            res=ffrt*fscd
        elif oper == "^":
            res=ffrt**fscd
        elif oper == "%":
            res=ffrt%fscd
        elif ValueError:
            print("wrong operation\ntry again")#if we have not +,-,/,*,^,% here we type wrong operation
            continue#this operation make the programm do 1st thing again
        print ("result:\n ", res)#\n - new line
    except ValueError:#if we have error on this stage we Printing wrong numbers and continueing
        print("wrong numbers \ntry again")
        continue
