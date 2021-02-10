#user can reg backend database will be created
from tkinter import *
import os

from tkinter import messagebox
te=Tk()
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
te.geometry('300x200')
L1 = Label(text = "User Name").grid(row=1,column=0)
E1 = Entry( te)
E1.grid(row=1,column=2)
L2 = Label(text="full Name").grid(row=2,column=0)
E2 = Entry( te)
E2.grid(row=2,column=2)
L3 = Label(text="email").grid(row=3,column=0)
E3 = Entry( te)
E3.grid(row=3,column=2)
L4 = Label(text="admission no.").grid(row=4,column=0)
E4 = Entry(te)
E4.grid(row=4,column=2)
L5 = Label(text="password").grid(row=5,column=0)
E5 = Entry(te)
E5.grid(row=5,column=2)
def adduser():

    def check():
        if os.path.isfile(E1.get()):
            L6 = Label(text="username already taken")
            L6.place(x=50, y=130)
            te.after(2000, L6.destroy)
        else:
            add = open(E1.get(), "a+")
            add.write(E5.get() + ":")
            regex ='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
            if E2.get().isalpha():
                add.write(E2.get() + ":")
            else:
                L6 = Label(text="name can only contain letters, recheck")
                L6.place(x=50, y=130)
                te.after(2000, L6.destroy)
            if (re.search(regex,E3.get())):
                add.write(E1.get()+":")
                add.write(E3.get() + ":")
                add.write(E4.get())
                B5.config(state="disabled")

                messagebox.showinfo("Congratulation!!", 'registraion susscefull')
                B6 = Button(text="  login  ", command=main)
                B6.grid(row=6, column=1)
            else:
                L6 = Label(text="invalid email, recheck")
                L6.place(x=50, y=130)
                te.after(2000, L6.destroy)
    check()
def main():
    te.destroy()
    os.system("Login.py")
B5=Button(text="register",command=adduser)
B5.grid(row=6,column=1)
te.mainloop()