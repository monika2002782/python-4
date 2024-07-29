# import socket
# from tkinter import*


# r=Tk()
# r.title("client and server")
# r.geometry("500x500")
# l=Label(r,text="port_address").place(relx=0.1,rely=0.1)
# e=Entry(r).place(relx=0.288,rely=0.1)

# def click():
#     s=socket.socket()
#     host=socket.gethostname()
#     port=34523
#     s.connect((host,port))
#     a=s.recv(1024)
#     print(a.decode()+"i am a client five")
#     s.close()
# b=Button(r,text="connect",command=lambda:click()).place(relx=0.2,rely=0.2)
# r.mainloop()
