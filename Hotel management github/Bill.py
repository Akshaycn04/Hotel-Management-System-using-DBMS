from tkinter import *
import mysql.connector
from checkout import *
from datetime import datetime

menu = Tk()
menu.title("Bill")
menu.geometry("500x700")
menu.configure(background='white')


def bill():
    cnx = mysql.connector.connect(host="localhost",user="root",password="",database="")
    cur = cnx.cursor()
    a=f"SELECT Quantity1,Qty2,Qty3 from fooddetails where RoomNo={Roomno}"
    cur.execute(a)
    B=cur.fetchone()
    BF=B[0]
    Lun=B[1]
    Din=B[2]
    c=f"SELECT Roomtype,Checkindate,Checkoutdate,CustomerName from Custdetails where Roomnumber={Roomno}"
    cur.execute(c)
    D=cur.fetchone()
    roomtype=D[0]
    checkindate=D[1]
    checkoutdate=D[2]
    custname=D[4]
    d1=datetime.strptime(checkindate,"%d-%m-%y")
    d2=datetime.strptime(checkoutdate,"%d-%m-%y")
    d3=(d2-d1).days
    bfprice=BF*d3*50
    Lunchprice=Lun*d3*150
    Dinprice=Din*d3*150
    food=bfprice+Lunchprice+Dinprice
    if roomtype=='single':
        roomprice=d3*750
    else:
        roomprice=d3*1000
    total=food+roomprice
    tax=.18*total
    total2=total+tax
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
    Label(menu, text="______", font=("Aerial",20), bg='white').place(x=340, y=390)
    Label(menu, text="______", font=("Aerial",20), bg='white').place(x=340, y=440)
    Label(menu, text="Total:", font=("Aerial",20), bg='white').place(x=20, y=430)
    Label(menu, text="Thank You", font=("Rockwell",25), bg='white').place(x=175, y=550)
    Label(menu, text="Visit us again", font=("Rockwell",25), bg='white').place(x=150,y=590)
    Label(menu, text=custname, font=("Aerial",20), bg='white').place(x=110, y=160)
    Label(menu, text=Roomno, font=("Aerial",20), bg='white').place(x=210, y=210)
    Label(menu, text=roomprice, font=("Aerial",20), bg='white').place(x=350, y=260)
    Label(menu, text=food, font=("Aerial",20), bg='white').place(x=350, y=310)
    Label(menu, text=tax, font=("Aerial",20), bg='white').place(x=350, y=360)
    Label(menu, text=total2, font=("Aerial",20), bg='white').place(x=350, y=430)

    menu.mainloop()


bill()
Label(menu, text="The Aviary", font=("Rockwell",30), bg='white').place(x=130, y=20)
Label(menu, text="Bill:", font=("Rockwell",28), bg='white').place(x=20, y=90)
Label(menu, text="Name:", font=("Aerial",20), bg='white').place(x=20, y=160)
Label(menu, text="Room Number:", font=("Aerial",20), bg='white').place(x=20, y=210)
Label(menu, text="Accomodation:", font=("Aerial",20), bg='white').place(x=20, y=260)
Label(menu, text="Food Cost:", font=("Aerial",20), bg='white').place(x=20, y=310)
Label(menu, text="Tax(18%):", font=("Aerial",20), bg='white').place(x=20, y=360)
Label(menu, text="______", font=("Aerial",20), bg='white').place(x=340, y=390)
Label(menu, text="______", font=("Aerial",20), bg='white').place(x=340, y=440)
Label(menu, text="Total:", font=("Aerial",20), bg='white').place(x=20, y=430)
Label(menu, text="Thank You", font=("Rockwell",25), bg='white').place(x=175, y=550)
Label(menu, text="Visit us again", font=("Rockwell",25), bg='white').place(x=150,y=590)
Label(menu, text=custname, font=("Aerial",20), bg='white').place(x=110, y=160)
Label(menu, text=Roomno, font=("Aerial",20), bg='white').place(x=210, y=210)
Label(menu, text=roomprice, font=("Aerial",20), bg='white').place(x=350, y=260)
Label(menu, text=food, font=("Aerial",20), bg='white').place(x=350, y=310)
Label(menu, text=tax, font=("Aerial",20), bg='white').place(x=350, y=360)
Label(menu, text=total2, font=("Aerial",20), bg='white').place(x=350, y=430)

menu.mainloop()
