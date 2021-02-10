#this contain code of booking and deleting and seeing ur booking
from tkinter import *
from tkinter import messagebox
import sqlite3
import os
import os.path
con=sqlite3.Connection("Booking")
cur=con.cursor()
cur.execute("create table if not exists Booking(username varchar(20),address varchar(56),mob number(10),qty number(2),Book varchar(50))")
def sr():
    te = Tk()
    te.geometry("500x500")
    L1 = Label(text = "User Name").grid(row=1,column=0)
    E1 = Entry(te)
    E1.grid(row=1,column=2)
    L2 = Label(text="address").grid(row=2,column=0)
    E2 = Entry( te)
    E2.grid(row=2,column=2)
    L3 = Label(text="mob").grid(row=3,column=0)
    E3 = Entry( te)
    E3.grid(row=3,column=2)
    L4 = Label(text="qty number").grid(row=4,column=0)
    E4 = Entry(te)
    E4.grid(row=4,column=2)
    L5 = Label(text="book name").grid(row=5, column=0)
    E5 = Entry(te)
    E5.grid(row=5, column=2)
    def db():
        a = (E1.get(), E2.get(), E3.get(),E4.get(),E5.get())
        if os.path.isfile(E1.get()):
            if os.path.isfile(E5.get()):
                cur.execute("insert into Booking values(?,?,?,?,?)", a)
                con.commit()
                cur.execute("select * from Booking")
                a = cur.fetchall()
                ab = int(E4.get())
                if os.path.isfile(E5.get()):
                    r=open("d1")
                    f=r.read().split(":")
                    cost=int(f[1])
                    ac = ab * cost
                    messagebox.showinfo("Congratulation!!", "Your oreder value is %s" % ac)
                    print(a)
                te.destroy()
                os.system("library.py")
            else:
                messagebox.showinfo("ERROR","we dont have this book in our stock" )
        else:
            messagebox.showinfo("ERROR","username invalid")
    b161=Button(text="confirm booking",command=db)
    b161.place(x=200,y=200)
    te.mainloop()
def sw():
    te = Tk()
    te.geometry("250x300")
    L1 = Label(text="User Name").grid(row=1, column=0)
    E1 = Entry(te)
    E1.grid(row=1, column=2)
    def db():
        if os.path.isfile(E1.get()):
            cur.execute("select * from Booking where username=?", (E1.get(),))
            a = cur.fetchall()
            messagebox.showinfo('Find', a)

            te.destroy()
            os.system("library.py")
        else:
            messagebox.showinfo("ERROR","username invalid")
    b161 = Button(text="search booking", command=db)
    b161.place(x=100, y=100)
    te.mainloop()
def sdw():
    te = Tk()
    te.geometry("250x300")
    L1 = Label(text="User Name").grid(row=1, column=0)
    E1 = Entry(te)
    E1.grid(row=1, column=2)
    L5 = Label(text="book name").grid(row=5, column=0)
    E5 = Entry(te)
    E5.grid(row=5, column=2)
    def db():
        if os.path.isfile(E1.get()):
            st="DELETE  from Booking where username='%s' and Book='%s'"%(E1.get(),E5.get())
            cur.execute(st)
            con.commit()
            messagebox.showinfo('Find', " booking deleted")
            te.destroy()
            os.system("library.py")
        else:
            messagebox.showinfo("ERROR","username invalid")
    b161 = Button(text="Delete booking", command=db)
    b161.place(x=100, y=100)
    te.mainloop()
