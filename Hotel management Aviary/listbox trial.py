from tkinter import *
from tkinter import ttk
 
root = Tk()
root.geometry("200x150")
 
frame = Frame(root)
frame.pack()
a=StringVar()
b=StringVar()
def vari(event):
    c=a.get()
    print(c)

def vari2(event):
    d=b.get()
    print(d)

 
vlist = ["Option1", "Option2", "Option3",
          "Option4", "Option5"]
 
Combo = ttk.Combobox(frame,state = "readonly", values = vlist,textvariable=a)
Combo.pack(padx = 5, pady = 5)
Combo.set("Number of People")
Combo.bind('<<ComboboxSelected>>',vari)

Combo2 = ttk.Combobox(frame,state = "readonly", values = vlist,textvariable=b)
Combo2.pack(padx = 6, pady = 6)
Combo2.set("Number of People")
Combo2.bind('<<ComboboxSelected>>',vari2)


 
root.mainloop()

