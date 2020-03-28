import socket

s = socket.socket()
print('Socket Created')

host = socket.gethostname()
port = 9999

s.bind( (host, port) )

s.listen(3) # 3 connection queue
print('waiting for connections')

while True:
    c,addr = s.accept() # returns client socket and address
    string = c.recv(1024).decode()

    print('Connected with ', addr)

    c.send(bytes(string.lower(),'utf-8'))

    c.close() # closing connection