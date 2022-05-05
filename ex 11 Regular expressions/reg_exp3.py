import re
data="From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
atpos = data.find ("@")
print (atpos)

sppos = data.find (' ', atpos) #find (substr, start, end) - we start at atpos
print (sppos)

host = data[atpos+1:sppos]
print (host)

lin = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y = re.findall('@([^ ]*)',lin)
#@ - look through string until find @
#( - started string extraction
#[^ ] - match non-blank (не пустые) character
#* - match many of them
#) - ended extraction
#so we have everything after "@" until we find first blank character
print (y)
import re
lin = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y = re.findall('^From .*@([^ ]*)',lin)
# ^From - we tryin to find string that started from "From "

print(y)
