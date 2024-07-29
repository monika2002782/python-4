import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=12345
s.bind((host,port))
s.listen(5)
while True:
    C,addr=s.accept()
    print("got connection from",addr)
    s1='''A client usually does not share any of its resources,
      but it requests content or service from a server.''' 
    C.send(s1.encode())
    C.close()