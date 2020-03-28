import socket
import threading
import sys

class Server:

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connections = []
    host = socket.gethostname()
    print("Server Host : ",host)
    port = 10000
    
    def __init(self):
        self.s.bind((self.host, self.port))
        print("Waiting for connections ... ")
        self.s.listen(1)



    def handler(self, c, a):
        while True:
            data = c.recv(1024)

            for connection in self.connections:
                connection.send(bytes(data,'utf-8'))

            if not data:
                print(str(a[0]) + ' : ' + str(a[1], " disconnected"))
                self.connections.remove(c)
                c.close()
                break

    def run(self):
        while True:
            try:
                c, a = self.s.accept()
            except:
                continue
            cThread = threading.Thread(target=self.handler, args=(c, a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(str(a[0]) + ' : ' + str(a[1]), " connected")

class Client:
    
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    port = 10000 

    def sendMsg(self):
        while True:
            self.c.send(bytes(input(""), 'utf-8'))

    def __init__ (self, host):
        self.c.connect((host, self.port))
        
        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()
        
        while True:
            data = self.c.recv(1024)
            if not data:
                break
            print(str(data, 'utf-8'))
    
    



def main():
    if (len(sys.argv)) > 1:
        client = Client(sys.argv[1])
    else:
        server = Server()
        server.run()
    
if __name__ == "__main__":
    main()