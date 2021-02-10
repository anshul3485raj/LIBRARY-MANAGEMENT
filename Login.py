#user can login
from tkinter import *
import os
import time
te=Tk()
te.geometry('300x200')
L1 = Label(text = "User Name")
L1.grid(row=1,column=0)
E1 = Entry(te)
E1.grid(row=1,column=2)
L5 = Label(text="password")
L5.grid(row=5,column=0)
E5 = Entry(te)
E5.grid(row=5,column=2)
def tr():
    d=E1.get()
    L7 = Label(text=d)
    L8 = Label(text="username=")
    L7.place(x=420, y=10)
    L8.place(x=350, y=10)
    te.geometry('500x500')
def rw():
    L9=Label(text='search your book')
    L9.place(x=70,y=65)
    E6=Entry(te)
    E6.place(x=70,y=65)
#def forget():
#   pass
def login():
    try:
        f=open(E1.get(),"r+")
        r=f.read().split(":")
        if E5.get() == r[0]:
            L1.grid_forget()
            E1.grid_forget()
            L5.grid_forget()
            E5.grid_forget()
            B6.grid_forget()
            B7.grid_forget()
            L7 = Label(text=r[2])
            L8 = Label(text="username=")
            L7.place(x=420, y=10)
            L8.place(x=350, y=10)
            te.geometry('500x500')
        if E5.get()!=r[0]:
            L6 = Label(text="recheck username and password")
            L6.place(x=50, y=70)
            te.after(2000, L6.destroy)
    except:
        L6= Label(text="recheck username and password")
        L6.place(x=50,y=70)
        te.after(2000, L6.destroy)
B6=Button(text="  login  ",command=login)
B6.grid(row=6,column=1)
#B7=Button(text="  forget  ",command=forget)
#B7.grid(row=7,column=1)
te.mainloop()