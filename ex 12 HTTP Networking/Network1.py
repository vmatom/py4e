#tcp - transport control protocol
#tcp port number - like a phone number

#application Protocol
# HTTP - Hypertext Transfer protocol. Invented for the web - to retrieve HTML, Images, Docs, etc...
# protocol is set of the rules.
#We'd try to make python web browser
#GET https://www.py4e.com/code3/mbox.txt
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) #data.pr4e.org - Host, 80 - port (HTTP)
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() #\r change position of carriage to begining of the line
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print (data.decode())
mysock.close()
