# Exercise 5: (Advanced) Change the socket program so that it only shows data after the headers and
# a blank line have been received. Remember that recv receives characters (newlines and all), not lines.
import socket

# This is using HTTP 1.0 - not all servers support the oldest protocol
# Try http://data.pr4e.org/romeo.txt if your server fails.
#url = ("http://data.pr4e.org/romeo.txt")
url = input('Enter: ')
words = url.split('/')
host = words[2]

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
mysock.send(('GET '+url+' HTTP/1.0\r\n\r\n').encode())
comp=str()
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    data = data.decode()
    posit = data.find("\r\n\r\n")
    print(data[posit+1:], end="")
    comp += data[posit+1:]
print (comp)
mysock.close()
