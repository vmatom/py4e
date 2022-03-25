str= 'X-DSPAM-Confidence: 0.8475 '
print(str)
dodot = str.find(":")
print(dodot)

num=str[dodot+1:]
print (num)

fnum=float(num)
print (fnum)
snuum=fnum+2
print (snuum)
