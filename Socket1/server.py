import socket

s = socket.socket()
print('Socket Created')

s.bind( ('localhost',9999) )

s.listen(3) # 3 connection queue
print('waiting for connections')

while True:
    c,addr = s.accept() # returns client socket and address
    print('Connected with ', addr)

    c.send(bytes("Weclome to Abhishek's server ",'utf-8'))

    c.close() # closing connection