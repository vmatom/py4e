print ("lp")
mmm = max
count = 0
total = 0
average = 0
for azura in [34, 35, 36, 37, 30, 502, 5021]: #azura is this numbers
    if azura < 35.5: #programm making all the numbers of azura from left to right
        count= count+1 #it is counting only succesful steps
        mmm = azura #we want to know what values more that 35,5
        total=azura+total#this is total value of numbers
#when if statement is true (don't forget that it is ignoring "30")
        average=total/count#can find average like this or make it in print
        print("count", count,"variable ", mmm,"total ", total,"average without var ", total/count,"average var ", average)
print (mmm)
print ("count of itteration is ", count)
print ("total we have ", total)
print ("average we have ",total/count, average)
