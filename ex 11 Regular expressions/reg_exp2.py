#^ Matches the begininning of a line
#$ Matches the end of a lines
#. Matches any characters
#\s Matches whitespace
#\S Matches any non-whitespace character
#* Repeats a character zero or more times
#*? Repeats a character zero or more times (non-greedy)
#+ Repeats a character one or more times
#+? Repeats a character one or more times (non-greedy)
#[aeiou] Matches a single character in the listed set
#[^XYZ] Matches a single character not in the listed set
#[a-z0-9] The set of characters can include a range
#( Indicates where string extraction is to start
#) Indicated where string extraction is to end
#to import regular expressions you need to "import re"
import re
x = "My 2 favorite numbers are 19 and 42"
y= re.findall('[0-9]+', x)
print (y)
y= re.findall('[AEIOU]+', x)
print (y)
y= re.findall('[aeiou]+', x)
print (y)
y= re.findall('[a-z]+', x)
print (y)
x = "From: Using the : characters"
y= re.findall('F.+:', x)#here is greedy matching. It's tryied to find biggest example
print (y)
y= re.findall('^F.+?:', x)#here is nongreedy matching. It's tryied to find smallest example
print (y)
hand2 = open('search.txt')
for line2 in hand2:
    line2 = line2.rstrip()
    y= re.findall('\S+@\S+', line2)
    #print (y)
#Fine-tuning string extraction
#parantheses are not part of the match - but they tell where to start and stop what string to extract
    y= re.findall('^From (\S+@\S+)', line2) #Started from "From" and have a "@" to find
    #print (y)
    if len (y) < 1:
        continue
    else:
        print (y)
