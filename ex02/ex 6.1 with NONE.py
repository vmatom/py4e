mmm = None
print ("started ",mmm)
count = 0
total = 0
average = 0
for azura in [34, 35, 36, 37, 30, 502, 5021]:
    if mmm is None:#if mmm "IS" not "=="
    #here we checking mmm. If mmm is none we will change mmm to azura
    #it could be "is not" as well.
        mmm = azura
#else when azura is less than value of mmm that equal 1st value of azura
    elif azura<mmm:
        mmm = azura
    print(azura, mmm)
print("at least ", mmm)
#IS is the more strong type of ==
