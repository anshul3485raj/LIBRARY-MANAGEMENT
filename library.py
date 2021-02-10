#this is library from here u can read or rent a book
from tkinter import *
import os
import book
import sqlite3
import os
t=Tk()
t.geometry("755x600")
text=Label(text="library")
text.place()
def book1():
    t.destroy()
    book.sr()
def read():
    os.startfile("Encyclopedia of Comic Books and Graphic Novels ( PDFDrive ).pdf")
def read1():
    os.startfile("Coraline Graphic Novel ( PDFDrive ).pdf")
def read2():
    os.startfile("Survivors - A Novel of the Coming Collapse ( PDFDrive ).pdf")
def read3():
    os.startfile("The Essential Rumi by Coleman Barks ( PDFDrive ).pdf")
def read4():
    os.startfile("The Gifts of Imperfection_ Embrace Who You Are ( PDFDrive ).pdf")
def read5():
    os.startfile("The Year of the Flood_ A Novel ( PDFDrive ).pdf")
def read6():
    os.startfile("Then She Was Gone_ A Novel ( PDFDrive ).pdf")
def read7():
    os.startfile("The fault in our star.pdf")
#textsection
L10=Label(text='Encyclopedia of Comic Books')
L10.place(x=1,y=1)
L11=Label(text='Coraline Graphic Novel')
L11.place(x=200,y=1)
L12=Label(text='Survivors ')
L12.place(x=400,y=1)
L13=Label(text='The Essential Rumi')
L13.place(x=600,y=1)
L14=Label(text='The Gifts of Imperfection')
L14.place(x=1,y=200)
L15=Label(text='The Year of the Flood')
L15.place(x=200,y=200)
L16=Label(text='Then She Was Gone')
L16.place(x=400,y=200)
L17=Label(text='The fault in our star')
L17.place(x=600,y=200)
#book Button
b9=Button(text="book",command=book1)
b9.place(x=1,y=60)
b10=Button(text="book",command=book1)
b10.place(x=200,y=60)
b11=Button(text="book",command=book1)
b11.place(x=400,y=60)
b12=Button(text="book",command=book1)
b12.place(x=600,y=60)
b13=Button(text="book",command=book1)
b13.place(x=1,y=260)
b14=Button(text="book",command=book1)
b14.place(x=200,y=260)
b15=Button(text="book",command=book1)
b15.place(x=400,y=260)
b16=Button(text="book",command=book1)
b16.place(x=600,y=260)
#readhere
b91=Button(text="Read",command=read)
b91.place(x=1,y=100)
b101=Button(text="Read",command=read1)
b101.place(x=200,y=100)
b111=Button(text="Read",command=read2)
b111.place(x=400,y=100)
b121=Button(text="Read",command=read3)
b121.place(x=600,y=100)
b131=Button(text="Read",command=read4)
b131.place(x=1,y=300)
b141=Button(text="read",command=read5)
b141.place(x=200,y=300)
b151=Button(text="Read",command=read6)
b151.place(x=400,y=300)
b161=Button(text="Read",command=read7)
b161.place(x=600,y=300)
def rt():
    t.destroy()
    book.sw()
def rtw():
    t.destroy()
    book.sdw()
b162 = Button(text="show booking", command=rt)
b162.place(x=300, y=450)
b163 = Button(text="delete booking", command=rtw)
b163.place(x=200, y=450)
t.mainloop()