from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os


menu = Tk()
menu.title("The Aviary")
menu.geometry("1920x1080")
menu.configure(background='#cb9499')

canvas=Canvas(
    menu,
    width=1920,
    height=450
    )
canvas.pack()
img=(Image.open("Add the path of the related photo"))
resized_image=img.resize((1600,600), Image.Resampling.LANCZOS)
new_image=ImageTk.PhotoImage(resized_image)
canvas.create_image(0,0, anchor=NW, image=new_image)

Label(menu, text="The Aviary", font=("Algerian",30), bg='#cb9499').place(x=660, y=455)
Label(menu, text="The luxury you deserve",font=("Algerian",30), bg='#cb9499').place(x=550, y=510)


def Checkin():
    menu.destroy()
    import Usercheckin

def Custcare():
    menu.destroy()
    import custcare

def aurelia():
    menu.destroy()
    import fooddet

def Exit():
    os._exit(0)

def back():
    menu.destroy()
    import Main

Button(menu,
       text="Back",
       command=back,height = 2, width = 15).place(x=920, y=750)
    
    

Button(menu,
       text="Aurelia Kitchen",
       command=aurelia,height = 3, width = 20,).place(x=700, y=620)
    

Button(menu,
       text="Check-in",
       command=Checkin,height = 3, width = 20).place(x=100, y=620)



Button(menu,
       text="Exit",
       command=Exit,height = 2, width = 15).place(x=520, y=750)
    

Button(menu,
       text="Customer Care",
       command=Custcare,height = 3, width = 20).place(x=1300, y=620)



menu.mainloop()
os.system('user.py')

