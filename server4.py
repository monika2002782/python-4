import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=12354
s.bind((host,port))
s.listen(5)
while True:
    C,addr=s.accept()
    print("got connection from",addr)
    s1='''A client usually does not share any of its resources'''
    C.send(s1.encode())
    C.close()