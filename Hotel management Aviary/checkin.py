from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
import random

def Checkin():
    if Var1.get()==1:
        Roomtype='single'
    else:
        Roomtype='double'
        
        
    CustomerName = e1.get()
    PhoneNumber = e2.get()
    Address= e3.get()
    EmailID= e4.get()
    Checkindate= e6.get()
    Checkoutdate = e7.get()
    Roomnumber=random.randint(1,100)

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="")
    mycursor=mysqldb.cursor()
    mycursor.execute("select count(*) from Custdetails where Roomtype=\"single\"")
    data=mycursor.fetchone()
    for i in data:
        roomsingle=i
    mycursor.execute("select count(*) from Custdetails where Roomtype=\"double\"")
    data=mycursor.fetchone()
    for j in data:
        roomdouble=j
    if CustomerName == '' or PhoneNumber== 0 or Address == '' or EmailID == '' or Roomtype == '' or Checkindate=='' or Checkoutdate=='':
        messagebox.showwarning("Warning", "Incomplete Data Entry")
    elif Roomtype=="single":
        if roomsingle < 5:
            try:
                sql = "INSERT INTO Custdetails () VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                val = (CustomerName,PhoneNumber,Address,EmailID,Roomtype,Checkindate,Checkoutdate,Roomnumber)
                mycursor.execute(sql, val)
                mysqldb.commit()
                sql2 = "INSERT INTO details () VALUES (%s, %s, %s, %s, %s)"
                val2 = (CustomerName,Roomnumber,Checkindate,Checkoutdate,Roomtype)
                mycursor.execute(sql2, val2)
                mysqldb.commit()
                messagebox.showinfo("Congrats",f"Your room number is {Roomnumber}")
                
                
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()
        else:
            messagebox.showinfo("oops", "There is no vacant room available")
            
    
    elif Roomtype=="double":
        if roomdouble < 10:
            try:
                sql = "INSERT INTO Custdetails () VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                val = (CustomerName,PhoneNumber,Address,EmailID,Roomtype,Checkindate,Checkoutdate,Roomnumber)
                mycursor.execute(sql, val)
                mysqldb.commit()
                sql2 = "INSERT INTO details () VALUES (%s, %s, %s, %s, %s)"
                val2 = (CustomerName,Roomnumber,Checkindate,Checkoutdate,Roomtype)
                mycursor.execute(sql2, val2)
                mysqldb.commit()
                messagebox.showinfo("Congrats",f"Your room number is {Roomnumber}")
        
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()
        else:
            messagebox.showinfo("oops", "There is no vacant room available")
            
        
root = Tk()
root.title("Hotel check-in")
root.geometry("1920x1080")
root.configure(background='grey')
global e1
global e2
global e3
global e4
global e5
global e6
global e7



Label(root, text="Customer Name", font=("Times New Roman",15), bg='grey').place(x=100, y=290)
Label(root, text="Phone Number", font=("Times New Roman",15), bg='grey').place(x=100, y=340)
Label(root, text="Address", font=("Times New Roman",15), bg='grey').place(x=100, y=390)
Label(root, text="Email ID", font=("Times New Roman",15), bg='grey').place(x=100, y=440)
Label(root, text="Type of room", font=("Times New Roman",15), bg='grey').place(x=100, y=490)
Label(root, text="Check-in date", font=("Times New Roman",15), bg='grey').place(x=100, y=540)
Label(root, text="Check-out date", font=("Times New Roman",15), bg='grey').place(x=100, y=590)
Label(root, text="The Aviary ", font=("Algerian",35), bg='grey').place(x=210, y=10)
Label(root, text="The luxury you deserve ", font=("Algerian",30), bg='grey').place(x=130, y=70)
Label(root, text="Check-in Credentials", font=("Century Gothic",30), bg='grey').place(x=100, y=200)
Label(root, text="₹7,500", font=("Times New Roman",15), bg='grey',fg='black').place(x=640, y=520)
Label(root, text="₹10,000", font=("Times New Roman",15), bg='grey',fg='black').place(x=500, y=520)

e1 = Entry(root)
e1.place(x=500, y=295,width=200,height=25)

e2 = Entry(root)
e2.place(x=500, y=345,width=200,height=25)

e3 = Entry(root)
e3.place(x=500, y=395,width=200,height=25)

e4 = Entry(root)
e4.place(x=500, y=445,width=200,height=25)


e6 = Entry(root)
e6.place(x=500, y=545,width=200,height=25)

e7 = Entry(root)
e7.place(x=500, y=595,width=200,height=25)

Var1 = BooleanVar()
Var2 = BooleanVar()
Button(root, text="Confirm", font=("Times New Roman",10), command=Checkin ,height = 2, width = 8).place(x=570, y=750)
c1=Checkbutton(root, text = "Single", variable = Var1,onvalue=True,offvalue=False)
c1.place(x=640, y=495)
c2=Checkbutton(root, text = "Double", variable = Var2,onvalue=True,offvalue=False)
c2.place(x=500, y=495)


def close():
    root.destroy()
    import menu2


Button(
    root, 
    text="Back", 
    command=close,
    height = 2, width = 8
    ).place(x=100,y=750)


canvas=Canvas(
    root,
    width=750,
    height=1080
    )
canvas.pack(anchor=E)
img=(Image.open("Add the path of the related photo"))
resized_image=img.resize((750,800), Image.Resampling.LANCZOS)
new_image=ImageTk.PhotoImage(resized_image)
canvas.create_image(0,0, anchor=NW, image=new_image)


root.mainloop()

