from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os


menu = Tk()
menu.title("The Aviary")
menu.geometry("1920x1080")
menu.configure(background='grey')

canvas=Canvas(
    menu,
    width=1920,
    height=450
    )
canvas.pack()
img=(Image.open("Add the path of the related photo"))
resized_image=img.resize((1600,600))
new_image=ImageTk.PhotoImage(resized_image)
canvas.create_image(0,0, anchor=NW, image=new_image)

Label(menu, text="The Aviary", font=("Rockwell",30), bg='grey').place(x=620, y=455)
Label(menu, text="ADMIN ACCESS", font=("Rockwell",25), bg='grey').place(x=590, y=510)


def Checkin():
    menu.destroy()
    import checkin
    

Button(menu,
       text="Check-in",
       command=Checkin,height = 3, width = 20).place(x=100, y=620)

def Customerdet():
    menu.destroy()
    import custdet
    

Button(menu,
       text="Customer Details",
       command=Customerdet,height = 3, width = 20).place(x=500, y=620)

def Checkout():
    menu.destroy()
    import checkout
    

Button(menu,
       text="Check-out",
       command=Checkout,height = 3, width = 20).place(x=900, y=620)

def Exit():
    os._exit(0)

Button(menu,
       text="Exit",
       command=Exit,height = 2, width = 15).place(x=520, y=750)

def foodet():
    menu.destroy
    import fooddetails

def back():
    menu.destroy()
    import Main

Button(menu,
       text="Back",
       command=back,height = 2, width = 15).place(x=920, y=750)
    

Button(menu,
       text="Food Package Details",
       command=foodet,height = 3, width = 20).place(x=1300, y=620)



menu.mainloop()
os.system('menu2.py')
