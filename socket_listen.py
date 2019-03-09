

# TODO make sure shebang is correct /bin/env?
#   /bin/env python3.6
import socket

s = socket.socket()

#host = socket.gethostname()
host = "192.168.33.10"      # works, but should use hostname
port = 80
s.bind((host,port))
s.listen(5)
while True:

    # connection and addess are returned
    c, addr = s.accept()
    print("Connection accepted from " + repr(addr[1]))

    # connection.send() needs what?
    c.send("Server approved connection\n".encode('utf-8'))
    print (repr(addr[1]) + ": " + c.recv(1026).decode())
    c.close()
