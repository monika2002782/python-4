import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=56894
s.bind((host,port))
s.listen(5)
while True:
    C,addr=s.accept()
    print("got connection from",addr)
    s1='''Examples of computer applications that use the client–server model are email,
        network printing, and the World Wide Web.'''
    C.send(s1.encode())
    C.close()