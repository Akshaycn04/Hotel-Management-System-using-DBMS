import tkinter as tk
from tkinter import ttk
from tkinter import *
import mysql.connector

def show():
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT * FROM Custdetails")
        records = mycursor.fetchall()
        
        for i, (CustomerName,PhoneNumber,Address,EmailID,Roomtype,Checkindate,Checkoutdate,Phonenumber) in enumerate(records, start=1):
            listBox.insert("", "end", values=(CustomerName,PhoneNumber,Address,EmailID,Roomtype,Checkindate,Checkoutdate,Phonenumber))
            mysqldb.close()


root = tk.Tk()
root.title("Customer Details")
root.geometry("1920x1080")
label = tk.Label(root, text="Customer Details", font=("Arial",30)).grid(row=0, columnspan=1)

cols = ('Customer Name', 'Phone Number', 'Address', 'Email ID', 'RoomType', 'Check-in date', 'Check-out date', 'Room Number')
listBox = ttk.Treeview(root, columns=cols, show='headings')
listBox.column("# 1",width=200)
listBox.column("# 2",width=120)
listBox.column("# 3",width=350)
listBox.column("# 4",width=230)
listBox.column("# 5",width=170)
listBox.column("# 6",width=170)
listBox.column("# 7",width=150)
listBox.column("# 8",width=150)
s=ttk.Style()
s.configure('Treeview', rowheight=40)

for col in cols:
    listBox.heading(col, text=col)    
    listBox.grid(row=1, column=0, columnspan=1)

def Close():
        root.destroy()
        import menu2

Button(root,
       text="close",
       command=Close,height = 3, width = 20).place(x=1378, y=737)
show()
root.mainloop()
