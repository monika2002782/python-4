import tkinter
from tkinter import*
from tkinter import ttk, font, messagebox
from PIL import  Image
from PIL.ImageTk import PhotoImage
import pymysql as mysql
import requests


def Tourpackages(r):
      
      r.destroy()
      r=Tk()
      r.geometry("1000x1000")
      r.attributes('-fullscreen', True)
      r.configure(bg="gray44")
      f=Frame(r,width=1500,height=50,bg="maroon1").pack()
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="METRO BOOKING",font=lf,bg="maroon1",fg="black")
      x.place(relx=0.4,rely=0.01)

      
      f=Frame(r,width=1500,height=1500)


      img=PhotoImage(Image.open("pic1.jpg"))
      x=Label(f,image=img).place(relx=0.040,rely=0.033)
      

      img1=PhotoImage(Image.open("pic2.jpg"))
      x=Label(f,image=img1).place(relx=0.040,rely=0.340)

       
      img2=PhotoImage(Image.open("pic3.jpg"))
      x=Label(f,image=img2).place(relx=0.040,rely=0.655)

         
      img3=PhotoImage(Image.open("pic4.jpg"))
      x=Label(f,image=img3).place(relx=0.5,rely=0.033)
      
        
      img4=PhotoImage(Image.open("pic5.jpg"))
      x=Label(f,image=img4).place(relx=0.5,rely=0.340)
      
        
      img5=PhotoImage(Image.open("pic6.jpg"))
      x=Label(f,image=img5).place(relx=0.5,rely=0.655)
      
      
      f.pack()

      lf=font.Font(weight="bold",family="Times New Roman",size=10 )
      lf1=font.Font(weight="bold",family="Times New Roman",size=13 )
      x=Label(f,text="ROYAL MADHYA PRADESH EX MUMBAI",font=lf1,fg="purple1").place(relx=0.24,rely=0.033)
      x=Label(f,text="DURATION: 1 Night/2 Days",font=lf,fg="black").place(relx=0.28,rely=0.083)
      x=Label(f,text="ORIGIN: Ahmedabad",font=lf,fg="black").place(relx=0.28,rely=0.135)
      x=Label(f,text="DEPARTURE: Daily",font=lf,fg="black").place(relx=0.28,rely=0.190) 
      x=Label(f,text="UPCOMING JOURNEY: 23-jul-24",font=lf,fg="black").place(relx=0.28,rely=0.235) 


      lf=font.Font(weight="bold",family="Times New Roman",size=10 )
      lf1=font.Font(weight="bold",family="Times New Roman",size=13 )
      x=Label(f,text="SIKKIM SILVER",font=lf1,fg="purple1").place(relx=0.28,rely=0.327)
      x=Label(f,text="DURATION: 5 Night/6 Days",font=lf,fg="black").place(relx=0.28,rely=0.378)
      x=Label(f,text="ORIGIN: Bagdogra",font=lf,fg="black").place(relx=0.28,rely=0.433)
      x=Label(f,text="DEPARTURE: Daily",font=lf,fg="black").place(relx=0.28,rely=0.493) 
      x=Label(f,text="UPCOMING JOURNEY: 23-jul-24",font=lf,fg="black").place(relx=0.28,rely=0.550) 



      lf=font.Font(weight="bold",family="Times New Roman",size=10 )
      lf1=font.Font(weight="bold",family="Times New Roman",size=13 )
      x=Label(f,text="UJJAIN OMKARESHWAR JYOTIRLINGA",font=lf1,fg="purple1").place(relx=0.24,rely=0.650)
      x=Label(f,text="DURATION: 2 Night/3 Days",font=lf,fg="black").place(relx=0.28,rely=0.710)
      x=Label(f,text="ORIGIN: Indore",font=lf,fg="black").place(relx=0.28,rely=0.760)
      x=Label(f,text="DEPARTURE: Daily",font=lf,fg="black").place(relx=0.28,rely=0.810) 
      x=Label(f,text="UPCOMING JOURNEY: 23-jul-24",font=lf,fg="black").place(relx=0.28,rely=0.865) 



      lf=font.Font(weight="bold",family="Times New Roman",size=10 )
      lf1=font.Font(weight="bold",family="Times New Roman",size=13 )
      x=Label(f,text="MATA VAISHNODEVI EX DELHI",font=lf1,fg="purple1").place(relx=0.72,rely=0.040)
      x=Label(f,text="DURATION: 3 Night/4 Days",font=lf,fg="black").place(relx=0.75,rely=0.090)
      x=Label(f,text="ORIGIN: Delhi",font=lf,fg="black").place(relx=0.75,rely=0.125)
      x=Label(f,text="DEPARTURE: Weekday",font=lf,fg="black").place(relx=0.75,rely=0.165) 
      x=Label(f,text="UPCOMING JOURNEY: 23-jul-24",font=lf,fg="black").place(relx=0.75,rely=0.200) 




      lf=font.Font(weight="bold",family="Times New Roman",size=10 )
      lf1=font.Font(weight="bold",family="Times New Roman",size=13 )
      x=Label(f,text="GOLDEN TRAIANGLE OF ODISHA",font=lf1,fg="purple1").place(relx=0.72,rely=0.330)
      x=Label(f,text="DURATION: 4 Night/5 Days",font=lf,fg="black").place(relx=0.75,rely=0.380)
      x=Label(f,text="ORIGIN: Bhubaneswar",font=lf,fg="black").place(relx=0.75,rely=0.420)
      x=Label(f,text="DEPARTURE: Dailey",font=lf,fg="black").place(relx=0.75,rely=0.470) 
      x=Label(f,text="UPCOMING JOURNEY: 23-jul-24",font=lf,fg="black").place(relx=0.75,rely=0.510) 



      lf=font.Font(weight="bold",family="Times New Roman",size=10 )
      lf1=font.Font(weight="bold",family="Times New Roman",size=13 )
      x=Label(f,text="SUNDAR SAURASHTRA AHMEDABAD",font=lf1,fg="purple1").place(relx=0.72,rely=0.650)
      x=Label(f,text="DURATION: 7 Night/8 Days",font=lf,fg="black").place(relx=0.75,rely=0.710)
      x=Label(f,text="ORIGIN: Ahmedabad",font=lf,fg="black").place(relx=0.75,rely=0.760)
      x=Label(f,text="DEPARTURE: Dailey",font=lf,fg="black").place(relx=0.75,rely=0.810) 
      x=Label(f,text="UPCOMING JOURNEY: 23-jul-24",font=lf,fg="black").place(relx=0.75,rely=0.865) 





      lf=font.Font(weight="bold",family="Times New Roman",size=20 )
      b=Button(r,text="Quit",font=lf,bg="steelblue1",fg="black",command=lambda:finish()).place(relx=0.910,rely=0.840)
       
      
      f=Frame(r,width=1500,height=51,bg="maroon1").place(relx=0,rely=0.940)
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="@EXPRESS 3/28",font=lf,bg="maroon1",fg="black").place(relx=0.4,rely=0.94)
      
      def finish():
           messagebox.showinfo("Thank You!!!","^^Your Successfully Visited Empire Builder Express^^")
           exit()


      r.mainloop()



def Bookingdetails(r):
       


      r.destroy()
      r=Tk()
      r.geometry("1000x1000")
      r.attributes('-fullscreen', True)
      r.configure(bg="gray44")
      f=Frame(r,width=1500,height=50,bg="dark slate blue").pack()
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="METRO BOOKING",font=lf,bg="dark slate blue",fg="black")
      x.place(relx=0.4,rely=0.01)

       


      f=Frame(r,width=1500,height=1500,bg="gray51")
      img1=PhotoImage(Image.open("t3.jpg"))
      x=Label(f,image=img1).place(relx=0.033,rely=0.1)
      
      img=PhotoImage(Image.open("book4.jpg"))
      x=Label(f,image=img).place(relx=0.250,rely=0)
      
      f.pack()

      lf4=font.Font(weight="bold",family="Times New Roman",size=15 )



      
      x=Label(r,text="^^Happy Journey^^",font=lf,bg="gray51",fg="white").place(relx=0.018,rely=0.070)
      x=Label(r,text="!!!Travailing in Empire Builder",font=lf4,bg="gray51",fg="white").place(relx=0.030,rely=0.550) 
      x=Label(r,text="Express is an Unbelievable",font=lf4,bg="gray51",fg="white").place(relx=0.030,rely=0.580)  
      x=Label(r,text="Experience,as they give you",font=lf4,bg="gray51",fg="white").place(relx=0.030,rely=0.610)  
      x=Label(r,text="a royal feel at every step off",font=lf4,bg="gray51",fg="white").place(relx=0.030,rely=0.640) 
      x=Label(r,text="the journey.I suggest, every",font=lf4,bg="gray51",fg="white").place(relx=0.030,rely=0.670)  
      x=Label(r,text="traveler should experience this",font=lf4,bg="gray51",fg="white").place(relx=0.030,rely=0.7) 
      x=Label(r,text="once in a life time!!!",font=lf4,bg="gray51",fg="white").place(relx=0.030,rely=0.730)
      x=Label(r,text="^^Thank You^^",font=lf,bg="gray51",fg="white").place(relx=0.018,rely=0.8)
      
      
      
      
      x=Label(f,text="Booking Details",font=lf,bg="white").place(relx=0.560,rely=0.150)
      lf=font.Font(weight="bold",family="Times New Roman",size=17)
      x=Label(r,text="Source",width=10, height=1,font=lf,bg="white").place(relx=0.366,rely=0.330)
      x=Label(r,text="Destination",width=10, height=1,font=lf,bg="white").place(relx=0.366,rely=0.4)
      x=Label(r,text="General",width=10, height=1,font=lf,bg="white").place(relx=0.366,rely=0.470)
      x=Label(r,text="Date",width=10, height=1,font=lf,bg="white").place(relx=0.366,rely=0.550)
      x=Label(r,text="Selectcases",width=10, height=1,font=lf,bg="white").place(relx=0.680,rely=0.330)
      x=Label(r,text="TicketType",width=10, height=1,font=lf,bg="white").place(relx=0.680,rely=0.470)
      x=Label(r,text="Passenger",width=10, height=1,font=lf,bg="white").place(relx=0.680,rely=0.4)

      combo=ttk.Combobox(r,values=["Ladies","Duty Pass","Tatkal","Premium Tatkal","Lower Berth/SR.Citizen","Person With Disability"])
      combo.place(relx=0.5,rely=0.470,width=180, height=25)
      combo1=ttk.Combobox(r,values=["AC First Class(1A)","Anubhuti Class(EA)","Vistadome AC(EV)","First Class(FC)","Sleeper","Second Sitting(2S)"])
      combo1.place(relx=0.8,rely=0.330,width=180,height=25)


      combo2=ttk.Combobox(r,values=["E type","Other"])
      combo2.place(relx=0.8,rely=0.470,width=140, height=25)


      combo3=ttk.Combobox(r,values=["1 to 5","1 to 10"])
      combo3.place(relx=0.8,rely=0.4,width=180, height=25)

      
      lf1=font.Font(weight="bold",family="Times New Roman",size=11)
      x=Label(r,text="Selectlist",width=10, height=1,font=lf,bg="white").place(relx=0.680,rely=0.550)
      combo4=ttk.Combobox(r,values=["Flexible With Date","Train With Available Berth","Railway Pass Concession","Person With Disability Concession"])
      combo4.place(relx=0.8,rely=0.550,width=180, height=25)

      
      a1=Entry(r)
      a1.place(relx=0.5,rely=0.330,width=180, height=25)
      b1=Entry(r)
      b1.place(relx=0.5,rely=0.4,width=180, height=25)
      d1=Entry(r)
      d1.place(relx=0.5,rely=0.540,width=180, height=25)
     
      def inserting():
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="kkk")
        cursor=connection.cursor()
        s="insert into t2(Source,Destination,General,Date,Selectcases,Passenger,TicketType,Selectlist)values(%s,%s,%s,%s,%s,%s,%s,%s)"
        t=(a1.get(),b1.get(),combo.get(),d1.get(),combo1.get(),combo3.get(),combo2.get(),combo4.get())
        cursor.execute(s,t)
        connection.commit()
        print(cursor.rowcount,"new row inserted",cursor.lastrowid)
        messagebox.showinfo("insert","insert successfully")
            
      def deleting():
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="kkk")
        cursor=connection.cursor()
        sql="delete from t2 where Source='"+a1.get()+"'"
        cursor.execute(sql)
        connection.commit()
        print(cursor.rowcount,"record(s)deleted")
        messagebox.showinfo("delete","delete successfully")
        Tourpackages(r)




      
      b=Button(r,text="Insert",font=lf,bg="white",fg="black",command=lambda:inserting()).place(relx=0.5,rely=0.7)
      b=Button(r,text="Delete",font=lf,bg="white",fg="black",command=lambda:deleting()).place(relx=0.6,rely=0.7)
      
      
      f=Frame(r,width=1500,height=51,bg="dark slate blue").place(relx=0,rely=0.940)
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="@EXPRESS 3/28",font=lf,bg="dark slate blue",fg="black").place(relx=0.4,rely=0.94)
      r.mainloop()



def live_status(train_no,r):
   
    r=Tk()
    r.title("Details")
    r.geometry("500x500")
    r.configure(bg="gray")
    base_url="https://rappid.in/apis/train.php?train_no={}".format(train_no)
    response=requests.get(base_url)
    train_status=response.json()
    Label(r,text="#####",bg="gray").pack()
    Label(r,text=" /t/t Train name:"+ train_status["train_name"],bg="gray").pack()
    Label(r,text="######",bg="gray").pack()
    for station_info in train_status["data"]:
        if station_info["is_current_station"]:
            l=Label(r,text="now station \t\t\t\t:"+station_info["station_name"],bg="gray").pack()
            l1=Label(r,text="distance from the starting \t:"+station_info["distance"],bg="gray").pack()
            l2=Label(r,text="timing /t/t/t/t :"+station_info["timing"],bg="gray").pack()
            l3=Label(r,text="delay /t/t/t/t :"+station_info["delay"],bg="gray").pack()
            l4=Label(r,text="platform no /t/t/t/t :"+station_info["platform"],bg="gray").pack()
            l5=Label(r,text="half timing /t/t/t/t :"+station_info["halt"],bg="gray").pack()
    else:
        l6=Label(r,text=station_info["station_name"],bg="gray").pack()
        l7=Label(r,text="####",bg="gray").pack()
        l8=Label(r,text="\t\tmessage updated:"+train_status["updated_time"],bg="gray").pack()
        l9=Label(r,text="###",bg="gray").pack()
        
        b=Button(r,text="Click",bg="salmon1",fg="black").place(relx=0.445,rely=0.4)
        

def location(r):
        r=Tk()
        r.title("Train")
        r.geometry("500x500")
        r.configure(bg="gray")
      
      
        lf=font.Font(weight="bold",family="Times New Roman",size=20)
        x=Label(r,text="Train No:",font=lf,bg="gray",fg="black")
        x.place(relx=0.360,rely=0.4)
        b1=Entry(r)
        b1.place(relx=0.5,rely=0.4,width=150,height=25)
        
        
       
        lf=font.Font(weight="bold",family="Times New Roman",size=20)
        b=Button(r,text="Enter",font=lf,bg="springgreen2",fg="black",command=lambda:live_status(b1.get(),r))
        b.place(relx=0.450,rely=0.520)
        
        r.mainloop(r)
      


def Available(r):
      r.destroy()
      r=Tk()
      r.geometry("1000x1000")
      r.attributes('-fullscreen', True)
      r.configure(bg="royal blue")
      f=Frame(r,width=1500,height=50,bg="lightblue3").pack()
      lf=font.Font(weight="bold",family="Times New Roman",size=25)
      x=Label(f,text="METRO BOOKING",font=lf,bg="lightblue3",fg="black")
      x.place(relx=0.4,rely=0.01)
      
      
      f=Frame(r,width=1500,height=1500)
      img=PhotoImage(Image.open("number.jpg"))
      x=Label(f,image=img).place(relx=0,rely=0)
      
      f.pack()



      x=Label(f,text="AVAILABILITY FOR TRAIN",font=lf,bg="royalblue1",fg="white").place(relx=0.340,rely=0.150)
      lf=font.Font(weight="bold",family="Times New Roman",size=17)
      x=Label(r,text="Train No: 15705 ",font=lf,bg="royalblue1",fg="white").place(relx=0.270,rely=0.330)
      x=Label(r,text="Train No: 12038 ",font=lf,bg="royalblue1",fg="white").place(relx=0.270,rely=0.4)
      x=Label(r,text="Train No: 19339 ",font=lf,bg="royalblue1",fg="white").place(relx=0.270,rely=0.470)
      x=Label(r,text="Train No: 14722 ",font=lf,bg="royalblue1",fg="white").place(relx=0.270,rely=0.550)
      x=Label(r,text="Train No: 09757 ",font=lf,bg="royalblue1",fg="white").place(relx=0.270,rely=0.620)
      
      
      
      x=Label(r,text="Train Name:  Champaran Humsafar Express",font=lf,bg="royalblue1",fg="white").place(relx=0.460,rely=0.330)
      x=Label(r,text="Train Name:  Shatabdi Express",font=lf,bg="royalblue1",fg="white").place(relx=0.460,rely=0.4)
      x=Label(r,text="Train Name:  Dahod Bhopal Intercity Express",font=lf,bg="royalblue1",fg="white").place(relx=0.460,rely=0.470)
      x=Label(r,text="Train Name:  Abohar Jodhpur Express ",font=lf,bg="royalblue1",fg="white").place(relx=0.460,rely=0.550)
      x=Label(r,text="Train Name:  Badgam Baramulla DEMU Express Special",font=lf,bg="royalblue1",fg="white").place(relx=0.460,rely=0.620)
      
      
      b=Button (r,text="Search",font=lf,bg="royalblue1",fg="white",command=lambda:location(r)).place(relx=0.4,rely=0.8)
      b=Button (r,text="Next",font=lf,bg="royalblue1",fg="white",command=lambda:Bookingdetails(r)).place(relx=0.5,rely=0.8)
      f=Frame(r,width=1500,height=51,bg="lightblue3").place(relx=0,rely=0.940)
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="@EXPRESS 3/28",font=lf,bg="lightblue3",fg="black").place(relx=0.4,rely=0.94)

      

      r.mainloop()




def adminlogin(r):
       

      r.destroy()
      r=Tk()
      r.geometry("1000x1000")
      r.attributes('-fullscreen', True)
      r.configure(bg="gray44")
      f=Frame(r,width=1500,height=50,bg="saddle brown").pack()
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="METRO BOOKING",font=lf,bg="saddle brown",fg="black")
      x.place(relx=0.4,rely=0.01)

    
      f=Frame(r,width=1500,height=1500)
      img=PhotoImage(Image.open("admin.jpg"))
      x=Label(f,image=img).place(relx=0,rely=0)
      f.pack()

      


      
      f=Frame(r,width=350,height=690,bg="sandy brown").place(relx=0.745,rely=0.065)
      img1=PhotoImage(Image.open("admins.jpg"))
      x=Label(f,image=img1).place(relx=0.810,rely=0.2)




      x=Label(f,text="Login",font=lf,bg="sandy brown",fg="black").place(relx=0.840,rely=0.098)
      lf=font.Font(weight="bold",family="Times New Roman",size=17)
      x=Label(r,text="User Name",font=lf,bg="sandy brown").place(relx=0.780,rely=0.590)
      x=Label(r,text="Password",font=lf,bg="sandy brown").place(relx=0.780,rely=0.650)

     
      a1=Entry(r)
      a1.place(relx=0.880,rely=0.590,width=140, height=25)
      b1=Entry(r,show="*")
      b1.place(relx=0.880,rely=0.650,width=140, height=25)
      c1=Entry(r)

      def check(r):
        m1=a1.get()
        n1=b1.get()
        f=open("bk.txt","r")
        time=f.read()
        lines=time.split("\n")
        for line in lines:
            info=line.split()
            if info[0]==m1 and info[1]==n1:
                print("login")
                messagebox.showinfo("hello","login successfully")
                Available(r)
                break
            else:
                print("invaild")
                messagebox.showinfo("hello","invaild")
                break
            

      b=Button (r,text="Submit",font=lf,bg="saddle brown",fg="black",command=lambda:check(r)).place(relx=0.850,rely=0.730)
     
      f=Frame(r,width=1500,height=51,bg="saddle brown").place(relx=0,rely=0.940)
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="@EXPRESS 3/28",font=lf,bg="saddle brown",fg="black").place(relx=0.4,rely=0.94)

      r.mainloop()




         


def customerregister(r):
      r.destroy()
      r=Tk()
      r.geometry("1000x1000")
      r.attributes('-fullscreen', True)
      r.configure(bg="gray44")
      f=Frame(r,width=1500,height=50,bg="MediumPurple1").pack()
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="METRO BOOKING",font=lf,bg="MediumPurple1",fg="black")
      x.place(relx=0.4,rely=0.01)

      f=Frame(r,width=1500,height=1500,bg="gray44")
      img=PhotoImage(Image.open("customer.jpg"))
      x=Label(f,image=img).place(relx=0,rely=0) 

      f.pack() 


    
      x=Label(f,text="CustomerRegistration",bg="gray70",fg="black",font=lf,).place(relx=0.390,rely=0.130)
      lf=font.Font(weight="bold",family="Times New Roman",size=17)
      x=Label(r,text="Name",font=lf,width=10, height=1,bg="gray70",fg="black").place(relx=0.2,rely=0.330  )
      x=Label(r,text="Age",font=lf,width=10, height=1,bg="gray70",fg="black").place(relx=0.2,rely=0.4)
      x=Label(r,text="Gender",font=lf,width=10, height=1,bg="gray70",fg="black").place(relx=0.2,rely=0.470)
      x=Label(r,text="City",font=lf,width=10, height=1,bg="gray70",fg="black").place(relx=0.2,rely=0.540)
      x=Label(r,text="Nationality",font=lf,width=10, height=1,bg="gray70",fg="black").place(relx=0.2,rely=0.620)
      x=Label(r,text="Status",font=lf,width=10, height=1,bg="gray70",fg="black").place(relx=0.2,rely=0.690)
      x=Label(r,text="Pincode",font=lf,width=10, height=1,bg="gray70",fg="black").place(relx=0.560,rely=0.330)
      x=Label(r,text="Pho_no",font=lf,width=10, height=1,bg="gray70",fg="black").place(relx=0.560,rely=0.4)
      x=Label(r,text="Aadhar_no",font=lf,width=10, height=1,bg="gray70",fg="black").place(relx=0.560,rely=0.470)
      x=Label(r,text="Email_id",font=lf,width=10, height=1,bg="gray70",fg="black").place(relx=0.560,rely=0.540)
      x=Label(r,text="Pancard_no",font=lf,width=10, height=1,bg="gray70",fg="black").place(relx=0.560,rely=0.620)
      x=Label(r,text="Address",font=lf,width=10, height=1,bg="gray70",fg="black").place(relx=0.560,rely=0.690)
     

      var=IntVar()
      radio=Radiobutton(r,text="Male",variable=var,value=1)
      radio.place(relx=0.360,rely=0.470)
      radio=Radiobutton(r,text="Female",variable=var,value=2)
      radio.place(relx=0.440,rely=0.470)

      combo=ttk.Combobox(r,values=["indian","Indonesian","Iranian","Italian","Jordanian","Korean","Lithuanian ","Nigerian ","Other"])
      combo.place(relx=0.360,rely=0.620,width=180,height=25)

      combo1=ttk.Combobox(r,values=["Married","Unmarried"])
      combo1.place(relx=0.360,rely=0.690,width=180, height=25)
      
      a1=Entry(r)
      a1.place(relx=0.360,rely=0.330,width=180, height=25)
      b1=Entry(r)
      b1.place(relx=0.360,rely=0.4,width=180, height=25)
      d1=Entry(r)
      d1.place(relx=0.360,rely=0.540,width=180, height=25)
      g1=Entry(r)
      g1.place(relx=0.730,rely=0.330,width=180, height=25)
      h1=Entry(r)
      h1.place(relx=0.730,rely=0.4,width=180, height=25)
      i1=Entry(r)
      i1.place(relx=0.730,rely=0.470,width=180, height=25)
      j1=Entry(r)
      j1.place(relx=0.730,rely=0.540,width=180, height=25)
      k1=Entry(r)
      k1.place(relx=0.730,rely=0.620,width=180, height=25)
      l1=Entry(r)
      l1.place(relx=0.730,rely=0.690,width=180, height=60)
      

      def insert():
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="monika")
        cursor=connection.cursor()
        s="insert into t(Name,Age,City,Nationality,Status,Pincode,Pho_no,Adhar_no,Email_id,Pancard_no,Address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        t=(a1.get(),b1.get(),d1.get(),combo.get(),combo1.get(),g1.get(),h1.get(),i1.get(),j1.get(),k1.get(),l1.get())
        cursor.execute(s,t)
        connection.commit()
        print(cursor.rowcount,"new row inserted",cursor.lastrowid)
        messagebox.showinfo("insert","insert successfully")
        
      def delete():
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="monika")
        cursor=connection.cursor()
        sql="delete from t where name='"+a1.get()+"'"
        cursor.execute(sql)
        connection.commit()
        print(cursor.rowcount,"record(s)deleted")
        messagebox.showinfo("delete","delete successfully")

      def update():
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="monika")
        cursor=connection.cursor()
        sql="update t set Age='"+str(b1.get())+"',City='"+str(d1.get())+"',Nationality='"+str(combo.get())+"',Status='"+str(combo1.get())+"',Pincode='"+str(g1.get())+"',Pho_no='"+str(h1.get())+"',Adhar_no='"+str(i1.get())+"',Email_id='"+str(j1.get())+"',Pancard_no='"+str(k1.get())+"',Address='"+str(l1.get())+"'where Name='"+str(a1.get())+"'"
        cursor.execute(sql)
        connection.commit()
        print("updated in monika",sql)
        messagebox.showinfo("update","update successfully")
        adminlogin(r)



      b=Button(r,text="Insert",font=lf,bg="gray70",fg="black",command=lambda:insert()).place(relx=0.380,rely=0.8)
      b=Button(r,text="Delete",font=lf,bg="gray70",fg="black",command=lambda:delete()).place(relx=0.480,rely=0.8)
      b=Button(r,text="Update",font=lf,bg="gray70",fg="black",command=lambda:update()).place(relx=0.580,rely=0.8)
      f=Frame(r,width=1500,height=51,bg="MediumPurple1").place(relx=0,rely=0.940)
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="@EXPRESS 3/28",font=lf,bg="MediumPurple1",fg="black").place(relx=0.4,rely=0.94)

      r.mainloop()





def Next(r):
        r.destroy()
        r=Tk()
        r.geometry("1000x1000")
        r.attributes('-fullscreen', True)
        r.configure(bg="lightcyan3")
        f=Frame(r,width=1500,height=50,bg="lightblue4").pack()
        lf=font.Font(weight="bold",family="Times New Roman",size=25 )
        x1=Label(f,text="METRO BOOKING",font=lf,bg="lightblue4",fg="black")
        x1.place(relx=0.4,rely=0.01)

      
        f=Frame(r,width=1500,height=1500,bg="lightcyan3")
        img=PhotoImage(Image.open("detail1.jpg"))
        x=Label(f,image=img).place(relx=0.750,rely=0.015)
      

        img1=PhotoImage(Image.open("pack.jpg"))
        x=Label(f,image=img1).place(relx=0.750,rely=0.314)

       
        img2=PhotoImage(Image.open("exit.jpg"))
        x=Label(f,image=img2).place(relx=0.750,rely=0.620)

         
        img3=PhotoImage(Image.open("register1.jpg"))
        x=Label(f,image=img3).place(relx=0.5,rely=0.015)
      
        
        img4=PhotoImage(Image.open("login1.jpg"))
        x=Label(f,image=img4).place(relx=0.5,rely=0.305)
      
        
        img5=PhotoImage(Image.open("ava.jpg"))
        x=Label(f,image=img5).place(relx=0.5,rely=0.620)


        img6=PhotoImage(Image.open("front.jpg"))
        x=Label(f,image=img6).place(relx=0,rely=0)
      
      
        f.pack() 

        lf4=font.Font(weight="bold",family="Times New Roman",size=15 )

        b=Button(r,text="Customerregister",font=lf4,bg="gray70",fg="black",width=18,command=lambda:customerregister(r)).place(relx=0.515,rely=0.294)
        b=Button(r,text="Login",font=lf4,width=18,bg="gray70",fg="black",command=lambda:adminlogin(r)).place(relx=0.515,rely=0.585)
        b=Button(r,text="Trainavailability",font=lf4,width=18,bg="gray70",fg="black",command=lambda:Available(r)).place(relx=0.515,rely=0.876)
        b=Button(r,text="Bookingdetails",font=lf4,width=18,bg="gray70",fg="black",command=lambda:Bookingdetails(r)).place(relx=0.763,rely=0.3)
        b=Button(r,text="Tourpackages",font=lf4,width=18,bg="gray70",fg="black",command=lambda:Tourpackages(r)).place(relx=0.763,rely=0.590)
        b=Button(r,text="Exit",font=lf4,width=18,bg="gray70",fg="black",command=lambda:exit(r)).place(relx=0.763,rely=0.876)

        
      
        f=Frame(r,width=1500,height=51,bg="lightblue4").place(relx=0,rely=0.940)
        lf=font.Font(weight="bold",family="Times New Roman",size=25 )
        x=Label(f,text="@EXPRESS 3/28",font=lf,bg="lightblue4",fg="black").place(relx=0.4,rely=0.94)
        
        r.mainloop()





r=Tk()
r.title("Train")
r.attributes('-fullscreen', True)
r.configure(bg="gray1")
f=Frame(r,width=1500,height=98,bg="darkorchid4").pack()
lf=font.Font(weight="bold",family="Rockwell extra bold",size=45)
x=Label(f,text="EMPIRE BUILDER EXPRESS",font=lf,bg="darkorchid4",fg="white").place(relx=0.180,rely=0.012)


f=Frame(r,width=1500,height=1500).pack()
img=PhotoImage(Image.open("frontrain3.jpg"))
x=Label(f,image=img).place(relx=0,rely=0.128)

img1=PhotoImage(Image.open("l.jpg"))
x=Label(f,image=img1).place(relx=0,rely=0)




f=Frame(r,width=380,height=690,bg="gray51").place(relx=0.735,rely=0.130)
img2=PhotoImage(Image.open("l3.jpg"))
x=Label(f,image=img2).place(relx=0.785,rely=0.250)



img4=PhotoImage(Image.open("n6.jpg"))
x=Label(f,image=img4).place(relx=0.810,rely=0.922)


lf3=font.Font(weight="bold",family="Times New Roman",size=20 )
x=Label(f,text="Let The Adventure Begin!",font=lf3,bg="gray51",fg="white").place(relx=0.750,rely=0.170)

lf=font.Font(weight="bold",family="Times New Roman",size=25 )
x=Label(f,text="SAFETY!!",font=lf,bg="gray51",fg="white").place(relx=0.8,rely=0.580)
x=Label(f,text="SECURITY!!",font=lf,bg="gray51",fg="white").place(relx=0.8,rely=0.680)
x=Label(f,text="PUNCTUALITY!!",font=lf,bg="gray51",fg="white").place(relx=0.8,rely=0.780)
                        

lf=font.Font(weight="bold",family="Times New Roman",size=20 )
b=Button (r,text="Next",font=lf,bg="purple4",fg="white",command=lambda:Next(r))
b.place(relx=0.870,rely=0.922)


r.mainloop()





