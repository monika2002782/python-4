# import threading
# import time
# import socket
# def func():
#    s=socket.socket()
#    host=socket.gethostname()
#    print(host)
#    port=12345
#    s.bind((host,port))
#    s.listen(5)
#    while True:
#      c,addr=s.accept()
#      print("got connection from",addr)
#      s1="thank you for connecting"
#      c.send(s1.encode())
#      c.close()


# def func2():
#    s=socket.socket()
#    host=socket.gethostname()
#    port=12345
#    s.connect((host,port))
#    a=s.recv(1024)
#    print(a.decode()+"  I am a client one")
#    s.close()

# thread1=threading.Thread(target=func)
# thread2=threading.Thread(target=func2)
# thread1.start()
# thread2.start()
# thread2.join()
# thread1.join()