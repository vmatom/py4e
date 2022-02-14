data = "From    vmatom@gmail.com   14.02.2022"
tild=data.find("@")
print(tild)
spac=data.find("   ", tild)#tild is the place where you try to find
print(spac)
host = data[tild+1:spac] #from "tild" up to the "spac"
print(host)
