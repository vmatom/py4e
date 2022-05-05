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
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line) :#it is like line.startswith('From:')
        print (line)
import re
hand2 = open('search.txt')
for line2 in hand2:
    line2 = line2.rstrip()
    if re.search('^X-\S+:', line2) :#it is like line.startswith('From:')
        print (line2)
