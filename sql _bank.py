import tkinter
from tkinter import*
from tkinter import ttk, font, messagebox
from PIL import ImageTk,Image
import pymysql as mysql

def adminpage(r):
        r=Tk()
        r.geometry("1000x1000")
        r.attributes('-fullscreen', True)
        r.configure(bg="slate gray")
        f=Frame(r,width=1500,height=50,bg="firebrick1").pack()
        f=Frame(r,width=315,height=1800,bg="cyan").place(relx=0.0,rely=0.0)
        lf=font.Font(weight="bold",family="Times New Roman",size=25 )
        x=Label(f,text="CANARA BANK",font=lf,bg="firebrick1",fg="white")
        x.place(relx=0.5,rely=0.01)

        f=Frame(r,width=315,height=50,bg="blue").place(relx=0.0,rely=0.0)
        lf=font.Font(weight="bold",family="Times New Roman",size=25) 
        x=Label(f,text="SIDE PANEL",font=lf,bg="blue",fg="white").place(relx=0.04,rely=0.0)

        f=Frame(r,width=500,height=340,bg="khaki1").place(relx=0.430,rely=0.2)
        x=Label(f,text="CustomerRegistration",font=lf,bg="khaki1",fg="black").place(relx=0.485,rely=0.220)
        lf=font.Font(weight="bold",family="Times New Roman",size=17)
        x=Label(r,text="Mailid:",font=lf,bg="khaki1").place(relx=0.5,rely=0.330)
        

        with open("bk.txt","r")as f:
         time=f.read()
         print(time)
         lines=time.split("\n")
         for line in lines:
           Label(r,text=line.split("\t")[3]).place(relx=0.6,rely=0.340)
    


        lf=font.Font(weight="bold",family="Times New Roman",size=15 )
        lf=font.Font(weight="bold",family="Times New Roman",size=20 )
        b=Button(r,text="Admin login",font=lf,width=19,height=1,bg="DarkGoldenrod1",fg="black").place(relx=0.0,rely=0.2)
        b=Button(r,text="Customer login",font=lf,width=19,height=1,bg="DarkGoldenrod1",fg="black").place(relx=0.0,rely=0.4)
        b=Button(r,text="Customer Registration",font=lf,width=19,height=1,bg="DarkGoldenrod1",fg="black").place(relx=0.0,rely=0.6)
        b=Button(r,text="Exit",font=lf,bg="maroon1",fg="black",command=lambda:exit(r)).place(relx=0.089,rely=0.8)
        f=Frame(r,width=1500,height=50,bg="firebrick1").place(relx=0.230,rely=0.94)
        lf=font.Font(weight="bold",family="Times New Roman",size=25 )
        x=Label(f,text="MONIKA",font=lf,bg="firebrick1",fg="white").place(relx=0.5,rely=0.94)
        r.mainloop()

def func(a,b,r):
    r.destroy()
    if(a=="admin" and b=="admin"):
        adminpage(r)
    else:
        print("invaild")
        

def admin(r):
    r.destroy()
    r=Tk()
    r.geometry("1000x1000")
    r.attributes('-fullscreen', True)
    r.configure(bg="slate gray")
    f=Frame(r,width=1500,height=50,bg="firebrick1").pack()
    f=Frame(r,width=315,height=1800,bg="cyan").place(relx=0.0,rely=0.0)
    lf=font.Font(weight="bold",family="Times New Roman",size=25 )
    x=Label(f,text="CANARA BANK",font=lf,bg="firebrick1",fg="white")
    x.place(relx=0.5,rely=0.01)

    f=Frame(r,width=315,height=50,bg="blue").place(relx=0.0,rely=0.0)
    lf=font.Font(weight="bold",family="Times New Roman",size=25) 
    x=Label(f,text="SIDE PANEL",font=lf,bg="blue",fg="white").place(relx=0.04,rely=0.0)
    
    f=Frame(r,width=500,height=300,bg="palevioletRed1").place(relx=0.422,rely=0.3)
    x=Label(f,text="Admin login",font=lf,bg="palevioletRed1",fg="black").place(relx=0.545,rely=0.312)
    lf=font.Font(weight="bold",family="Times New Roman",size=17)
    a1=Label(f,text="Username:",font=lf,bg="palevioletRed1",fg="black").place(relx=0.474,rely=0.434)
    b1=Label(f,text="Password:",font=lf,bg="palevioletRed1",fg="black").place(relx=0.474,rely=0.5)
    a1=Entry(f)
    a1.place(relx=0.612,rely=0.435, width=150, height=25)
    b1=Entry(f,show="*")
    b1.place(relx=0.612,rely=0.5, width=150, height=25)
    b=Button(r,text="Login",font=lf,bg="thistle1",fg="black",command=lambda:func(a1.get(),b1.get(),r))
    b.place(relx=0.580,rely=0.612)

    lf=font.Font(weight="bold",family="Times New Roman",size=20 )
    b=Button(r,text="Admin login",font=lf,width=19,height=1,bg="DarkGoldenrod1",fg="black").place(relx=0.0,rely=0.2)
    b=Button(r,text="Customer login",font=lf,width=19,height=1,bg="DarkGoldenrod1",fg="black").place(relx=0.0,rely=0.4)
    b=Button(r,text="Customer Registration",font=lf,width=19,height=1,bg="DarkGoldenrod1",fg="black").place(relx=0.0,rely=0.6)
    b=Button(r,text="Exit",font=lf,bg="maroon1",fg="black",command=lambda:exit(r)).place(relx=0.089,rely=0.8)

    f=Frame(r,width=1500,height=50,bg="firebrick1").place(relx=0.230,rely=0.94)
    lf=font.Font(weight="bold",family="Times New Roman",size=25 )
    x=Label(f,text="MONIKA",font=lf,bg="firebrick1",fg="white").place(relx=0.5,rely=0.94)
    r.mainloop()

    
def loginpage(r,info):
        r.destroy()
        r=Tk()
        r.geometry("1000x1000")
        r.attributes('-fullscreen', True)
        r.configure(bg="slate gray")
        f=Frame(r,width=1500,height=50,bg="firebrick1").pack()
        f=Frame(r,width=315,height=1800,bg="cyan").place(relx=0.0,rely=0.0)
        lf=font.Font(weight="bold",family="Times New Roman",size=25 )
        x=Label(f,text="CANARA BANK",font=lf,bg="firebrick1",fg="white")
        x.place(relx=0.5,rely=0.01)

        f=Frame(r,width=315,height=50,bg="blue").place(relx=0.0,rely=0.0)
        lf=font.Font(weight="bold",family="Times New Roman",size=25) 
        x=Label(f,text="SIDE PANEL",font=lf,bg="blue",fg="white").place(relx=0.04,rely=0.0)

        f=Frame(r,width=500,height=540,bg="khaki1").place(relx=0.430,rely=0.150)
        x=Label(f,text="CustomerRegistration",font=lf,bg="khaki1",fg="black").place(relx=0.485,rely=0.220)
        lf=font.Font(weight="bold",family="Times New Roman",size=17)
        x=Label(r,text="Name:",font=lf,bg="khaki1").place(relx=0.480,rely=0.330)
        x=Label(r,text="Pho no:",font=lf,bg="khaki1").place(relx=0.480,rely=0.4)
        x=Label(r,text="Aadhar no:",font=lf,bg="khaki1").place(relx=0.480,rely=0.470)
        x=Label(r,text="Email id:",font=lf,bg="khaki1").place(relx=0.480,rely=0.550)
        x=Label(r,text="Pancard no:",font=lf,bg="khaki1").place(relx=0.480,rely=0.620)
        x=Label(r,text="Address:",font=lf,bg="khaki1").place(relx=0.480,rely=0.690)
        x=Label(r,text=info[0],font=lf,bg="khaki1").place(relx=0.6,rely=0.330)
        x=Label(r,text=info[1],font=lf,bg="khaki1").place(relx=0.6,rely=0.4)
        x=Label(r,text=info[2],font=lf,bg="khaki1").place(relx=0.6,rely=0.470)
        x=Label(r,text=info[3],font=lf,bg="khaki1").place(relx=0.6,rely=0.550)
        x=Label(r,text=info[4],font=lf,bg="khaki1").place(relx=0.6,rely=0.620)
        x=Label(r,text=info[5],font=lf,bg="khaki1").place(relx=0.6,rely=0.690)
        print(info)


        lf=font.Font(weight="bold",family="Times New Roman",size=15 )
        lf=font.Font(weight="bold",family="Times New Roman",size=20 )
        b=Button(r,text="Admin login",font=lf,width=19,height=1,bg="DarkGoldenrod1",fg="black").place(relx=0.0,rely=0.2)
        b=Button(r,text="Customer login",font=lf,width=19,height=1,bg="DarkGoldenrod1",fg="black").place(relx=0.0,rely=0.4)
        b=Button(r,text="Customer Registration",font=lf,width=19,height=1,bg="DarkGoldenrod1",fg="black").place(relx=0.0,rely=0.6)
        b=Button(r,text="Exit",font=lf,bg="maroon1",fg="black",command=lambda:exit(r)).place(relx=0.089,rely=0.8)
        f=Frame(r,width=1500,height=50,bg="firebrick1").place(relx=0.230,rely=0.94)
        lf=font.Font(weight="bold",family="Times New Roman",size=25 )
        x=Label(f,text="MONIKA",font=lf,bg="firebrick1",fg="white").place(relx=0.5,rely=0.94)
        r.mainloop()


        # def  customerlogin1(r):
        #     connection=mysql.connect(host="localhost",user="root",password="livewire",database="mysqll")
        #     cursor=connection.cursor()
        #     result="select * from mn5 where Name='"+a1.get()+"'and Contact='"+b1.get()+"'"
        #     cursor.execute(result)
        #     print(result)
        #     r=0
        #     for x in cursor:
        #         loginpage(x,r)
        #         r=r+1
        #     if r>0:
        #         print("loggin")
        #     else:
        #         print("not loggin")
        # r.mainloop()      




def Customerlogin(r):
    r.destroy()
    r=Tk()
    r.geometry("1000x1000")
    r.attributes('-fullscreen', True)
    r.configure(bg="slate gray")
    f=Frame(r,width=1500,height=50,bg="firebrick1").pack()
    f=Frame(r,width=315,height=1800,bg="cyan").place(relx=0.0,rely=0.0)
    lf=font.Font(weight="bold",family="Times New Roman",size=25 )
    x=Label(f,text="CANARA BANK",font=lf,bg="firebrick1",fg="white")
    x.place(relx=0.5,rely=0.01)

    f=Frame(r,width=315,height=50,bg="blue").place(relx=0.0,rely=0.0)
    lf=font.Font(weight="bold",family="Times New Roman",size=25) 
    x=Label(f,text="SIDE PANEL",font=lf,bg="blue",fg="white").place(relx=0.04,rely=0.0)
    
    f=Frame(r,width=500,height=300,bg="SeaGreen").place(relx=0.422,rely=0.3)
    x=Label(f,text="Customerlogin",font=lf,bg="SeaGreen",fg="black").place(relx=0.522,rely=0.312)
    lf=font.Font(weight="bold",family="Times New Roman",size=17)
    x=Label(f,text="Username:",font=lf,bg="SeaGreen",fg="black").place(relx=0.474,rely=0.434)
    x=Label(f,text="Password:",font=lf,bg="SeaGreen",fg="black").place(relx=0.474,rely=0.5)
    m=Entry(f)
    m.place(relx=0.612,rely=0.435, width=150, height=25)
    n=Entry(f,show="*")
    n.place(relx=0.612,rely=0.50, width=150, height=25)

    def check(r):
        m1=m.get()
        n1=n.get()
        f=open("bk.txt","r")
        time=f.read()
        lines=time.split("\n")
        for line in lines:
            info=line.split()
            print(info)
            if info[0]==m1 and info[1]==n1:
                print("login")
                messagebox.showinfo("hello","login successfully")
                loginpage(r,info)
                break
            else:
                print("invaild")
                messagebox.showinfo("hello","invaild")
                break
            
            
    b=Button(r,text="Login",font=lf,bg="tan1",fg="black",command=lambda:check(r)).place(relx=0.580,rely=0.612)
    lf=font.Font(weight="bold",family="Times New Roman",size=20 )
    b=Button(r,text="Admin login",font=lf,width=19,height=1,bg="DarkGoldenrod1",fg="black").place(relx=0.0,rely=0.2)
    b=Button(r,text="Customer login",font=lf,width=19,height=1,bg="DarkGoldenrod1",fg="black").place(relx=0.0,rely=0.4)
    b=Button(r,text="Customer Registration",font=lf,width=19,height=1,bg="DarkGoldenrod1",fg="black").place(relx=0.0,rely=0.6)
    b=Button(r,text="Exit",font=lf,bg="maroon1",fg="black",command=lambda:exit(r)).place(relx=0.089,rely=0.8)

    f=Frame(r,width=1500,height=50,bg="firebrick1").place(relx=0.230,rely=0.94)
    lf=font.Font(weight="bold",family="Times New Roman",size=25 )
    x=Label(f,text="MONIKA",font=lf,bg="firebrick1",fg="white").place(relx=0.5,rely=0.94)
    r.mainloop()

    


def CustomerRegistration(r):
    r.destroy()
    r=Tk()
    r.geometry("1000x1000")
    r.attributes('-fullscreen', True)
    r.configure(bg="slate gray")
    f=Frame(r,width=1500,height=50,bg="firebrick1").pack()
    f=Frame(r,width=315,height=1800,bg="cyan").place(relx=0.0,rely=0.0)
    lf=font.Font(weight="bold",family="Times New Roman",size=25 )
    x=Label(f,text="CANARA BANK",font=lf,bg="firebrick1",fg="white")
    x.place(relx=0.5,rely=0.01)

    f=Frame(r,width=315,height=50,bg="blue").place(relx=0.0,rely=0.0)
    lf=font.Font(weight="bold",family="Times New Roman",size=25) 
    x=Label(f,text="SIDE PANEL",font=lf,bg="blue",fg="white").place(relx=0.04,rely=0.0)

    f=Frame(r,width=500,height=540,bg="khaki1").place(relx=0.430,rely=0.150)
    x=Label(f,text="CustomerRegistration",font=lf,bg="khaki1",fg="black").place(relx=0.485,rely=0.220)
    lf=font.Font(weight="bold",family="Times New Roman",size=17)
    x=Label(r,text="Name",font=lf,bg="khaki1").place(relx=0.480,rely=0.330)
    x=Label(r,text="Pho no",font=lf,bg="khaki1").place(relx=0.480,rely=0.4)
    x=Label(r,text="Aadhar no",font=lf,bg="khaki1").place(relx=0.480,rely=0.470)
    x=Label(r,text="Email id",font=lf,bg="khaki1").place(relx=0.480,rely=0.550)
    x=Label(r,text="Pancard no",font=lf,bg="khaki1").place(relx=0.480,rely=0.620)
    x=Label(r,text="Address",font=lf,bg="khaki1").place(relx=0.480,rely=0.690)
    a1=Entry(r)
    a1.place(relx=0.6,rely=0.330,width=180, height=25)
    b1=Entry(r)
    b1.place(relx=0.6,rely=0.4,width=180, height=25)
    c1=Entry(r)
    c1.place(relx=0.6,rely=0.470,width=180, height=25)
    d1=Entry(r)
    d1.place(relx=0.6,rely=0.540,width=180, height=25)
    e1=Entry(r)
    e1.place(relx=0.6,rely=0.620,width=180, height=25)
    f1=Entry(r)
    f1.place(relx=0.6,rely=0.690,width=180, height=40)

   

    lf=font.Font(weight="bold",family="Times New Roman",size=15 )
    lf=font.Font(weight="bold",family="Times New Roman",size=20 )
    b=Button(r,text="Admin login",font=lf,width=19,height=1,bg="DarkGoldenrod1",fg="black").place(relx=0.0,rely=0.2)
    b=Button(r,text="Customer login",font=lf,width=19,height=1,bg="DarkGoldenrod1",fg="black").place(relx=0.0,rely=0.4)
    b=Button(r,text="Customer Registration",font=lf,width=19,height=1,bg="DarkGoldenrod1",fg="black").place(relx=0.0,rely=0.6)
    b=Button(r,text="Exit",font=lf,bg="maroon1",fg="black",command=lambda:exit(r)).place(relx=0.089,rely=0.8)

    def insert():
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="mysqll")
        cursor=connection.cursor()
        s="insert into mn5(Name,Phono,AdharNo,EmailId,PancardNo,Address)values(%s,%s,%s,%s,%s,%s)"
        t=(a1.get(),b1.get(),c1.get(),d1.get(),e1.get(),f1.get())
        cursor.execute(s,t)
        connection.commit()
        print(cursor.rowcount,"new row inserted",cursor.lastrowid)
        messagebox.showinfo("insert","insert successfully")
        
    def delete():
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="mysqll")
        cursor=connection.cursor()
        sql="delete from mn5 where name='"+a1.get()+"'"
        cursor.execute(sql)
        connection.commit()
        print(cursor.rowcount,"record(s)deleted")
        messagebox.showinfo("delete","delete successfully")

    def update():
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="mysqll")
        cursor=connection.cursor()
        sql="update mn5 set Phono='"+str(b1.get())+"',AdharNo='"+str(c1.get())+"',EmailId='"+str(d1.get())+"',PancardNo='"+str(e1.get())+"',Address='"+str(f1.get())+"'where name='"+str(a1.get())+"'"
        cursor.execute(sql)
        connection.commit()
        print("updated in moni",sql)
        messagebox.showinfo("update","update successfully")

    b=Button(r,text="insert",bg="blue",fg="white",command=lambda:insert()).place(relx=0.5,rely=0.9)
    b=Button(r,text="delete",bg="blue",fg="white",command=lambda:delete()).place(relx=0.6,rely=0.9)
    b=Button(r,text="update",bg="blue",fg="white",command=lambda:update()).place(relx=0.7,rely=0.9)


    f=Frame(r,width=1500,height=50,bg="firebrick1").place(relx=0.230,rely=0.94)
    lf=font.Font(weight="bold",family="Times New Roman",size=25 )
    x=Label(f,text="MONIKA",font=lf,bg="firebrick1",fg="white").place(relx=0.5,rely=0.94)
    r.mainloop()



#home
r=Tk()
r.title("Bank")
r.geometry("1000x1000")
r.attributes('-fullscreen', True)
r.configure(bg="slate gray")
f=Frame(r,width=1500,height=50,bg="deep pink").pack()
f=Frame(r,width=315,height=1800,bg="cyan").place(relx=0.0,rely=0.0)
lf=font.Font(weight="bold",family="Times New Roman",size=25 )
x=Label(f,text="CANARA BANK",font=lf,bg="deep pink",fg="white").place(relx=0.5,rely=0.01)

f=Frame(r,width=315,height=50,bg="blue").place(relx=0.0,rely=0.0)
lf=font.Font(weight="bold",family="Times New Roman",size=25) 
x=Label(f,text="SIDE PANEL",font=lf,bg="blue",fg="white").place(relx=0.04,rely=0.0)

lf=font.Font(weight="bold",family="Times New Roman",size=20 )
w="""Canara Bank is a state-owned commercial bank with headquarters in Bangalore.
The Bank provides a range of products and services to the customers.
Canara Bank is the third largest Public Sector Bank in India. """
x=Label(r,text=w,font=lf,bg="slate gray",fg="white")
x.place(relx=0.27,rely=0.1)

f=Frame(r,width=500,height=50)
f.place(relx=0.279,rely=0.3)
img=ImageTk.PhotoImage(Image.open("Canara-Bank-Limited-Logo.webp"))
x=Label(f,image=img)
x.pack()

lf=font.Font(weight="bold",family="Times New Roman",size=20 )
b=Button(r,text="Admin login",font=lf,width=19,height=1,bg="DarkGoldenrod1",fg="black",command=lambda:admin(r)).place(relx=0.0,rely=0.2)
b=Button(r,text="Customer login",font=lf,width=19,height=1,bg="DarkGoldenrod1",fg="black",command=lambda:Customerlogin(r)).place(relx=0.0,rely=0.4)
b=Button(r,text="Customer Registration",font=lf,width=19,height=1,bg="DarkGoldenrod1",fg="black",command=lambda:CustomerRegistration(r)).place(relx=0.0,rely=0.6)
b=Button(r,text="Exit",font=lf,bg="red",fg="black",command=lambda:exit(r)).place(relx=0.089,rely=0.8)

f=Frame(r,width=1500,height=50,bg="deep pink").place(relx=0.230,rely=0.94)
lf=font.Font(weight="bold",family="Times New Roman",size=25 )
x=Label(f,text="MONIKA",font=lf,bg="deep pink",fg="white").place(relx=0.5,rely=0.94)
r.mainloop()
