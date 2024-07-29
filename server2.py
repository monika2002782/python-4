import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=54321
s.bind((host,port))
s.listen(5)
while True:
    C,addr=s.accept()
    print("got connection from",addr)
    s1='''Clients, therefore, initiate communication sessions with servers, 
      which await incoming requests.'''
    C.send(s1.encode())
    C.close()