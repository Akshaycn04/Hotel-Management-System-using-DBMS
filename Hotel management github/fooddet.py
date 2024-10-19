from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("Aurelia Kitchen")
root.geometry("1920x1080")
root.configure(background='#1B609D')

def confirm():
    if Vr4.get()!=0 and Vr4.get()!="Number of People":
        Breakfast='Yes'
        qty1=Vr4.get()
    else:
        Breakfast='No'
        qty1=0
    if Vr5.get()!=0 and Vr5.get()!='Number of People':
        Lunch='Yes'
        qty2=Vr5.get()
    else:
        Lunch='No'
        qty2=0
    if Vr6.get()!=0 and Vr6.get()!="Number of People":
        Dinner='Yes'
        qty3=Vr6.get()
    else:
        Dinner='No'
        qty3=0

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="")
    mycursor=mysqldb.cursor()
    roomnum=e1.get()
    sql = "INSERT INTO fooddetails () VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (roomnum,Breakfast,qty1,Lunch,qty2,Dinner,qty3)
    mycursor.execute(sql, val)
    mysqldb.commit()
    messagebox.showinfo("Congrats","Reservation is booked")

e1=Entry(root)
e1.place(x=450, y=255,width=30,height=18)

Vr1 = BooleanVar()
Vr2 = BooleanVar()
Vr3 = BooleanVar()
Vr4 = StringVar()
Vr5 = StringVar()
Vr6 = StringVar()
c1=Checkbutton(root,text="₹450",variable=Vr1,onvalue=True,offvalue=False, bg='white')
c1.place(x=300, y=305)
c2=Checkbutton(root,text="₹650",variable=Vr2,onvalue=True,offvalue=False, bg='white')
c2.place(x=300, y=345)
c3=Checkbutton(root,text="₹750",variable=Vr3,onvalue=True,offvalue=False, bg='white')
c3.place(x=300, y=385)
Label(root, text="Aurelia Kitchen", font=("Algerian",35), bg='#1B609D').place(x=210, y=10)
Label(root, text="~The Aviary", font=("Times New Roman",26), bg='#1B609D').place(x=380, y=70)
Label(root, text="Table Reservation:", font=("Times New Roman",28), bg='#1B609D',fg='white').place(x=100, y=185)
Label(root, text="Break Fast", font=("Times New Roman",15), bg='#1B609D',fg='white').place(x=100, y=300)
Label(root, text="Lunch", font=("Times New Roman",15), bg='#1B609D',fg='white').place(x=100, y=340)
Label(root, text="Dinner", font=("Times New Roman",15), bg='#1B609D',fg='white').place(x=100, y=380)
Label(root, text="Enter Room Number", font=("Times New Roman",15), bg='#1B609D',fg='white').place(x=100, y=250)
Label(root, text="We feature dishes from around the globe, most cooked live and to your preference!", font=("arial",15), bg='#1B609D',fg='white').place(x=8, y=530)

Label(root, text="The Aurelia Kitchen is also the new music venue, playing your favourite music LIVE", font=("arial",15), bg='#1B609D',fg='white').place(x=8, y=560)


Label(root, text="The delicacies at the Aurelia Kitchen is a local favourite,", font=("arial",15), bg='#1B609D',fg='white').place(x=8, y=500)
vlist = ["1", "2", "3","4"]
 
Combo = ttk.Combobox(root,state = "readonly", values = vlist,textvariable=Vr4)
Combo.place(x=450,y=305)
Combo.set("Number of People")
def vari(event):
    BF=Vr4.get()
Combo.bind('<<ComboboxSelected>>',vari)

Combo2 = ttk.Combobox(root,state = "readonly", values = vlist,textvariable=Vr5)
Combo2.place(x=450,y=345)
Combo2.set("Number of People")
def vari2(event):
    Lun=Vr5.get()
Combo2.bind('<<ComboboxSelected>>',vari2)

Combo3 = ttk.Combobox(root,state = "readonly", values = vlist,textvariable=Vr6)
Combo3.place(x=450,y=385)
Combo3.set("Number of People")
def vari3(event):
    Din=Vr6.get()
Combo3.bind('<<ComboboxSelected>>',vari3)


def close():
    root.destroy()
    import User


Button(
    root, 
    text="Back", 
    command=close,
    height = 2, width = 8
    ).place(x=100,y=650)

Button(
    root, 
    text="Confirm", 
    command=confirm,
    height = 2, width = 8
    ).place(x=570,y=650)


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
