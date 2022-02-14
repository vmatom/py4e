print ("lp")
finding = False #need to make from capital letter
print ("before", finding)
for azura in [34, 35, 36, 37, 30, 502, 5021]: #azura is this numbers
    if azura == 37: #programm making all the numbers of azura from left to right
        finding=True #if azura would = 37 finding var became True.
        #after this moment finding became true
        #this makes us to check value of 37 is it exists in azuras variables
        if finding == True:#when we find azura = 37 we print it and break the line
        #breaking all code to make
            print("printed",azura)
            break
    print(finding,azura)#we print all loops before we find TRUE and breaks it
print ("here we go again ", finding)
