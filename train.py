# import tkinter
# from tkinter import*
# from tkinter import ttk, font, messagebox
# from PIL import ImageTk,Image
# import requests

# def live_status(train_no,r):
   
#     r=Tk()
#     r.geometry("500x500")
#     base_url="https://rappid.in/apis/train.php?train_no={}".format(train_no)
#     response=requests.get(base_url)
#     train_status=response.json()
#     Label(r,text="#####").pack()
#     Label(r,text=" /t/t Train name:"+ train_status["train_name"]).pack()
#     Label(r,text="######").pack()
#     for station_info in train_status["data"]:
#         if station_info["is_current_station"]:
#             l=Label(r,text="now station \t\t\t\t:"+station_info["station_name"]).pack()
#             l1=Label(r,text="distance from the starting \t:"+station_info["distance"]).pack()
#             l2=Label(r,text="timing /t/t/t/t :"+station_info["timing"]).pack()
#             l3=Label(r,text="delay /t/t/t/t :"+station_info["delay"]).pack()
#             l4=Label(r,text="platform no /t/t/t/t :"+station_info["platform"]).pack()
#             l5=Label(r,text="half timing /t/t/t/t :"+station_info["halt"]).pack()
#     else:
#         l6=Label(r,text=station_info["station_name"]).pack()
#         l7=Label(r,text="####").pack()
#         l8=Label(r,text="\t\tmessage updated:"+train_status["updated_time"]).pack()
#         l9=Label(r,text="###").pack()

# def location():
#         r=Tk()
#         r.title("Train")
#         r.geometry("500x500")
#         r.attributes('-fullscreen', True)
#         r.configure(bg="cyan")
#         f=Frame(r,width=1500,height=60,bg="deep pink").pack()
#         ttf=font.Font(weight="bold",family="time new roman",size=35)
#         a=Label(r,text="Rail Way",font=ttf,fg="white",bg="deep pink")
#         a.place(relx=0.43,rely=0.0)
#         ttf=font.Font(weight="bold",family="times new roman",size=20)
#         b=Label(r,text="Train No:",font=ttf,bg="cyan",fg="black")
#         b.place(relx=0.360,rely=0.7)
#         b1=Entry(r)
#         b1.place(relx=0.5,rely=0.7,width=150,height=35)
#         img=ImageTk.PhotoImage(Image.open("train.jpg"))
#         c=Label(r,image=img).place(relx=0.320,rely=0.2)
#         ttf=font.Font(weight="bold",family="times new roman",size=20)
#         b=Button(r,text="Enter",font=ttf,bg="brown",fg="black",command=lambda:live_status(b1.get(),r))
#         b.place(relx=0.450,rely=0.8)
#         r.mainloop()
# location()




### train details

# import requests


# def get_live_train_status(trainno):
#     base_url = "https://rappid.in/apis/train.php?train_no={}".format(trainno)
#     response = requests.get(base_url)
#     data = response.json()
#     return data


# if __name__ == "__main__":
#     train_number = "16102"
#     train_status = get_live_train_status(train_number)
#     print("*****************************************************************************")
#     print("\t\tTrain Name : ",train_status["train_name"])
#     print("*****************************************************************************")
#     for station_info in train_status["data"]:


#         if station_info["is_current_station"]:
#             print("Now Station \t\t\t\t: ",station_info["station_name"])
#             print("Distance From the Starting \t: ",station_info["distance"])
#             print("Timing \t\t\t\t\t\t: ",station_info["timing"])
#             print("Delay \t\t\t\t\t\t: ",station_info["delay"])
#             print("Platform No \t\t\t\t: ",station_info["platform"])
#             print("Halt Timing \t\t\t\t: ",station_info["halt"])
#     print("*****************************************************************************")
#     print("\t\tMessage \t\t: ",train_status["message"])
#     print("\t\tMessage Updated : ",train_status["updated_time"])
#     print("*****************************************************************************")

