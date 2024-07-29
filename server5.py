import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=34523
s.bind((host,port))
s.listen(5)
while True:
    C,addr=s.accept()
    print("got connection from",addr)
    s1='''A client usually does not share any of its resources,
      but it requests content or service from a server. 
      Clients, therefore, initiate communication sessions with servers, 
      which await incoming requests. 
      Examples of computer applications that use the client–server model are email,
        network printing, and the World Wide Web.'''
    C.send(s1.encode())
    C.close()