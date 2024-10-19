from tkinter import *
from functools import partial
from tkinter import messagebox


def validateLogin():
    B=user.get()
    A=passw.get()
    
    if A=='1234' and B=='1234':
        tkWindow.destroy()
        import menu2
    else:
        messagebox.showwarning('ERROR','Incorrect Password')

def back():
    tkWindow.destroy()
    import Main

tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('admin access')
global passw
global user


Label(tkWindow, text="User Name").grid(row=0, column=0)
user = Entry(tkWindow)
user.grid(row=0, column=1)

Label(tkWindow,text="Password").grid(row=1, column=0)  
passw = Entry(tkWindow,show='*')
passw.grid(row=1, column=1)

loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=2)

backSButton = Button(tkWindow, text="Back",command=back).grid(row=4, column=0) 

tkWindow.mainloop()



