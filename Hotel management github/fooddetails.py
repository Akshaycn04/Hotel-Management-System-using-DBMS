import tkinter as tk
from tkinter import ttk
from tkinter import *
import mysql.connector

def show():
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT * FROM fooddetails")
        records = mycursor.fetchall()
        
        for i, (RoomNo,BreakFast,Quantity1,Lunch,Qty2,Dinner,Qty3) in enumerate(records, start=1):
            listBox.insert("", "end", values=(RoomNo,BreakFast,Quantity1,Lunch,Qty2,Dinner,Qty3))
            mysqldb.close()


root = tk.Tk()
root.title("Reservation Details")
root.geometry("1920x1080")
label = tk.Label(root, text="Reservation Details", font=("Arial",30)).grid(row=0, columnspan=1)

cols = ('Room Number', 'Break Fast','Numberof People', 'Lunch', 'NumberofPeople', 'Dinner', 'Number of People')
listBox = ttk.Treeview(root, columns=cols, show='headings')
listBox.column("# 1",width=220)
listBox.column("# 2",width=220)
listBox.column("# 3",width=220)
listBox.column("# 4",width=220)
listBox.column("# 5",width=220)
listBox.column("# 6",width=220)
listBox.column("# 7",width=220)
s=ttk.Style()
s.configure('Treeview', rowheight=40)

for col in cols:
    listBox.heading(col, text=col)    
    listBox.grid(row=1, column=0, columnspan=1)

def close():
        root.destroy()
        import menu2

Button(root,
       text="close",
       command=close,height = 3, width = 20).place(x=1378, y=737)

show()

root.mainloop()
