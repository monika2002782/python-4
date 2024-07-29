# from tkinter import*
# import socket
# import threading
# import time


# r=Tk()
# r.title(" server")
# r.geometry("500x500")
# l=Label(r,text="port_address").place(relx=0.1,rely=0.1)
# e=Entry(r).place(relx=0.288,rely=0.1)


# def server():
#     s=socket.socket()
#     host=socket.gethostname()
#     print(host)
#     port=12345
#     s.bind((host,port))
#     s.listen(5)
#     while True:
#         C,addr=s.accept()
#         print("got connection from",addr)
#         s1='''A client usually does not share any of its resources,
#         but it requests content or service from a server.''' 
#         C.send(s1.encode())
#         C.close()
# b=Button(r,text="connect",command=lambda:server()).place(relx=0.2,rely=0.2)
# r.mainloop()


# thread1=threading.Thread(target=server)
# thread1.start()
# thread1.join()

