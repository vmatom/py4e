print ("lp")
mmm = -1
count = 0
total = 0
average = 0
for azura in [34, 35, 36, 37, 30, 502, 5021]: #azura is this numbers
    if azura > mmm: #programm making all the numbers of azura from left to right
        count= count+1 #it is counting only succesful steps
        mmm = azura #if azura is more than mmm we change mmm value to the azura.
        total=azura+total#this is total value of numbers
#when if statement is true (don't forget that it is ignoring "30")
        average=total/count#can find average like this or make it in print
        print(count, mmm, total, total/count, average)
print (mmm)
print ("count of itteration is ", count)
print ("total we have ", total)
print ("average we have ",total/count, average)
