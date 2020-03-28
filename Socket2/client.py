import socket

c = socket.socket() 

host = socket.gethostname()
port = 9999

c.connect( (host, port) )

string = input('Enter message ')
c.send(bytes(string,'utf-8'))

print(c.recv(1024).decode())