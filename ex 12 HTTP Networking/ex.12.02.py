# Exercise 2: Change your socket program so that it counts the number of characters it has received and stops
# displaying any text after it has shown 3000 characters. The program should retrieve the entire document and
# count the total number of characters and display the count of the number of characters at the end of the document.
# urllib library in python that does all the socket work for us and makes web pages looks like a file
import urllib.request, urllib.error, urllib.parse
import socket
inp_address = input("Type URL you need to connect to: ")
text = str()
try:
    sinp_address = inp_address.split("/")
    print(sinp_address)
    sock = sinp_address[2]
    print(sock)
    inp_address = "GET " + inp_address + " HTTP/1.0\r\n\r\n"
    print(inp_address)
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((sock, 80))
    cmd = inp_address.encode()
    mysock.send(cmd)
    while True:
        fhand = mysock.recv(50)
        if len(fhand) < 1:
            break
        text = text + fhand.decode()
    mysock.close()
except:
    print("try another URL")
counts = dict()
counts_char = dict()
lel = 0
words = text.split()
try:
    for char in text:
        counts_char[char] = counts.get(char, 0) + 1
    for word in words:
        counts[word] = counts.get(word, 0) + 1
except:
    print("ended")
print("dictionary of words", counts , "\ndictionary of characters", counts_char)
print(text[:3000], "\n amount of characters - ", len(text))

#https://www.py4e.com/code3/mbox.txt
#http://www.py4inf.com/code/mbox-short.txt
#http://data.pr4e.org/romeo.txt