import tkinter as tk
from PIL import Image, ImageTk
import os


root = tk.Tk()
root.title("Main")
root.geometry("1920x1080")

img=(Image.open("Add the path of the related photo"))
resized_image=img.resize((1600,800), Image.Resampling.LANCZOS)
new_image=ImageTk.PhotoImage(resized_image)

label = tk.Label(root,i=new_image)
label.pack()

def usr():
    root.destroy()
    import User

def adm():
    root.destroy()
    import password
def cls():
    os._exit(0)

btn=tk.Button(root,text='Admin',bg='#0a7e8c',command=adm,height = 2, width = 15).place(x=1100,y=700)
btn2=tk.Button(root,text='User',bg='#0a7e8c',command=usr,height = 2, width = 15).place(x=1300,y=700)
btn3=tk.Button(root,text='Close',command=cls,height = 2, width = 15).place(x=10,y=750)

root.mainloop()
os.system('menu2.py')
