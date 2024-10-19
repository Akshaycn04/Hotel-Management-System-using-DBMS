from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
from datetime import datetime

def Checkout():
    Roomno = e7.get()
    Phoneno = e2.get()
    CustName = e1.get()
    cnx = mysql.connector.connect(host="localhost",user="root",password="",database="")
    cur = cnx.cursor()
    cnx.commit()
    if Roomno==0 or Phoneno==0 or CustName == "":
        messagebox.showwarning("Warning", "incomplete data entry")
    elif Roomno!=0 or Phoneno!=0 or CustName != "":
        delt = f"DELETE FROM Custdetails where Roomnumber={Roomno}"
        cur.execute(delt)
        cnx.commit()
        messagebox.showinfo("Congrats", "Check-out was successful")


def bill():
    Roomno=e7.get()
    cnx = mysql.connector.connect(host="localhost",user="root",password="kattisql@123",database="miniproject")
    cur = cnx.cursor()
    a=f"SELECT Quantity1,Qty2,Qty3 from fooddetails where RoomNo={Roomno}"
    cur.execute(a)
    B=cur.fetchone()
    BF=B[0]
    Lun=B[1]
    Din=B[2]
    c=f"SELECT roomtype,checkindate,checkoutdate,Custname from details where Roomnumber={Roomno}"
    cur.execute(c)
    D=cur.fetchone()
    roomtype=D[0]
    checkindate=D[1]
    checkoutdate=D[2]
    custname=D[3]
    d1=datetime.strptime(checkindate,"%d-%m-%y")
    d2=datetime.strptime(checkoutdate,"%d-%m-%y")
    d3=(d2-d1).days
    bfprice=BF*d3*450
    Lunchprice=Lun*d3*650
    Dinprice=Din*d3*750
    food=bfprice+Lunchprice+Dinprice
    if roomtype=='single':
        roomprice=d3*7500
    else:
        roomprice=d3*10000
    total=food+roomprice
    tax=.18*total
    total2=total+tax
    totalstr='₹'+str(total2)
    menu = Tk()
    menu.title("Bill")
    menu.geometry("500x700")
    menu.configure(background='white')
    Label(menu, text="The Aviary", font=("Rockwell",30), bg='white').place(x=130, y=20)
    Label(menu, text="Bill:", font=("Rockwell",28), bg='white').place(x=20, y=90)
    Label(menu, text="Name:", font=("Aerial",20), bg='white').place(x=20, y=160)
    Label(menu, text="Room Number:", font=("Aerial",20), bg='white').place(x=20, y=210)
    Label(menu, text="Accomodation:", font=("Aerial",20), bg='white').place(x=20, y=260)
    Label(menu, text="Food Cost:", font=("Aerial",20), bg='white').place(x=20, y=310)
    Label(menu, text="Tax(18%):", font=("Aerial",20), bg='white').place(x=20, y=360)
    Label(menu, text="________", font=("Aerial",20), bg='white').place(x=340, y=390)
    Label(menu, text="________", font=("Aerial",20), bg='white').place(x=340, y=440)
    Label(menu, text="Total:", font=("Aerial",20), bg='white').place(x=20, y=430)
    Label(menu, text="Thank You", font=("Rockwell",25), bg='white').place(x=175, y=550)
    Label(menu, text="Visit us again", font=("Rockwell",25), bg='white').place(x=150,y=590)
    Label(menu, text=custname, font=("Aerial",20), bg='white').place(x=110, y=160)
    Label(menu, text=Roomno, font=("Aerial",20), bg='white').place(x=210, y=210)
    Label(menu, text=float(roomprice), font=("Aerial",20), bg='white').place(x=350, y=260)
    Label(menu, text=float(food), font=("Aerial",20), bg='white').place(x=350, y=310)
    Label(menu, text=tax, font=("Aerial",20), bg='white').place(x=350, y=360)
    Label(menu, text=totalstr, font=("Aerial",20), bg='white').place(x=350, y=430)

    menu.mainloop()
            

root = Tk()
root.title("Hotel Check-out")
root.geometry("1920x1080")
root.configure(background='grey')
global e7
global e2
global e1



canvas=Canvas(
    root,
    width=800,
    height=1080
    )
canvas.pack(anchor=E)
img=(Image.open("Add the path of the related photo"))
resized_image=img.resize((800,850), Image.Resampling.LANCZOS)
new_image=ImageTk.PhotoImage(resized_image)
canvas.create_image(0,0, anchor=NW, image=new_image)

Label(root, text="The Aviary", font=("Algerian",35), fg='white', bg='grey').place(x=170, y=10)
Label(root, text="The luxury of you deserve ", font=("Algerian",30), fg='white', bg='grey').place(x=95, y=80)
Label(root, text="Thank you for choosing Hotel Cryxalis", font=("Century Gothic",25), fg='white', bg='grey').place(x=60, y=650)
Label(root, text="Please visit us again", font=("Century Gothic",25), fg='white', bg='grey').place(x=190, y=710)
Label(root, text="Check-out Credentials", font=("Century Gothic",25), fg='white', bg='grey').place(x=98, y=220)
Label(root, text="Customer Name", font=("Times New Roman",15), fg='white', bg='grey').place(x=100, y=300)
Label(root, text="Phone Number", font=("Times New Roman",15), fg='white', bg='grey').place(x=100, y=370)
Label(root, text="Room Number", font=("Times New Roman",15), fg='white', bg='grey').place(x=100, y=440)


e1 = Entry(root)
e1.place(x=325, y=300,width=200,height=25)

e2 = Entry(root)
e2.place(x=325, y=370,width=200,height=25)

e7 = Entry(root)
e7.place(x=325, y=440,width=200,height=25)

def close():
    root.destroy()
    import menu2


Button(
    root, 
    text="Back", 
    command=close,
    height = 2, width = 8
    ).place(x=100,y=500)


Button(root, text="Confirm", font=("Times New Roman",10), command=Checkout ,height = 2, width = 8).place(x=390, y=500)
Button(root, text="Bill", font=("Times New Roman",10), command=bill,height = 2, width = 8).place(x=500, y=500)

root.mainloop()
