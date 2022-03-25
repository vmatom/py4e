fhand= open('mbox-short.txt')
mails = list()
count=0
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') :continue
    count= count+1
    words = line.split()
    print (words[2])
    email = words[1]
    print(email)
    pieces =email.split('@')
    print(pieces)
    mails.append(email)
print(mails)
print("WE have ", count, " of the from rows")
