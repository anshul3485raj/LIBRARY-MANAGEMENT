#main start from here user can reg and login using button
from tkinter import *
import os
t=Tk()
t.geometry("150x150")
title=Label(text="library management")
msg=["pls login/ register","s","s","s","s"]
tw=Label(text=msg[0])
title.pack()
tw.pack()
def login():
    t.destroy()
    os.system('Login.py')
def reg():
    t.destroy()
    os.system('regg.py')
B1=Button(text="login",command=login)
B1.pack()
B2=Button(text="register",command=reg)
B2.pack()
t.mainloop()