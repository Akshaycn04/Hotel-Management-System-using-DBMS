from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
      
root = Tk()
root.title("Customer Care")
root.geometry("1920x1080")
root.configure(background='#e2d9cc')
global e1
global e2
global e3
global e4





Label(root, text="Customer Name", font=("Times New Roman",15), bg='#e2d9cc').place(x=100, y=290)
Label(root, text="Room Number", font=("Times New Roman",15), bg='#e2d9cc').place(x=100, y=340)

Label(root, text="Email Id", font=("Times New Roman",15), bg='#e2d9cc').place(x=100, y=390)
Label(root, text="Enter your Query", font=("Times New Roman",15), bg='#e2d9cc').place(x=100, y=440)
Label(root, text="The Aviary ", font=("Algerian",35), bg='#e2d9cc').place(x=210, y=10)
Label(root, text="The luxury of comfort ", font=("Century Gothic",30), bg='#e2d9cc').place(x=130, y=70)
Label(root, text="Customer care", font=("Century Gothic",30), bg='#e2d9cc').place(x=100, y=200)

Label(root, text="Your feedback is appreciated, feel free to give feedback. Thank you!", font=("Times New Roman",15), bg='#e2d9cc').place(x=100, y=505)
Label(root, text="For further support you can contact +91 9993339993 or mail us at aviary@gmail.com", font=("Times New Roman",15), bg='#e2d9cc').place(x=100, y=555)
e1 = Entry(root)
e1.place(x=500, y=295,width=200,height=25)

e2 = Entry(root)
e2.place(x=500, y=345,width=200,height=25)

e3 = Entry(root)
e3.place(x=500, y=395,width=200,height=25)

e4 = Entry(root)
e4.place(x=500, y=445,width=200,height=25)


def close():
    root.destroy()
    import User

def custcare():
    messagebox.showinfo("Thank You","We will reach out to you shortly")

Button(root, text="Confirm", font=("Times New Roman",10),command=custcare,height = 2, width = 8).place(x=570, y=650)

Button(
    root, 
    text="Back", 
    command=close,
    height = 2, width = 8
    ).place(x=100,y=650)


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

