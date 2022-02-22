def bank(a,years):
    x=0
    e=0
    while x<years:
        e=a+e+e*perc/100
        x=x+1
        print(x,e)
    return e

a = float(input("Say how much money you want to give to a bank "))
years = float(input("Say how many years you want to wait "))
perc = float(input("Say % that you'll have "))
#print("$ - ", a,"\nyears - ", years, "\n% - ", perc)
q = bank(a,years)
print (q)
