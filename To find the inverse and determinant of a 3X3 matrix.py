from tkinter import *
from fractions import Fraction
import time

root = Tk()
root.title("Determinant")
root.geometry("180x300")
e1 = Entry(root, width=5)
e1.place(x=20, y=20)
e2 = Entry(root, width=5)
e2.place(x=70, y=20)
e3 = Entry(root, width=5)
e3.place(x=120, y=20)
e4 = Entry(root, width=5)
e4.place(x=20, y=50)
e5 = Entry(root, width=5)
e5.place(x=70, y=50)
e6 = Entry(root, width=5)
e6.place(x=120, y=50)
e7 = Entry(root, width=5)
e7.place(x=20, y=80)
e8 = Entry(root, width=5)
e8.place(x=70, y=80)
e9 = Entry(root, width=5)
e9.place(x=120, y=80)

def determinant():
    k1 = e1.get()
    k2 = e2.get()
    k3 = e3.get()
    k4 = e4.get()
    k5 = e5.get()
    k6 = e6.get()
    k7 = e7.get()
    k8 = e8.get()
    k9 = e9.get()
    i1 = int(k1)
    i2 = int(k2)
    i3 = int(k3)
    i4 = int(k4)
    i5 = int(k5)
    i6 = int(k6)
    i7 = int(k7)
    i8 = int(k8)
    i9 = int(k9)
    a = i1 * (i5 * i9 - i6 * i8)
    b = i2 * (i4 * i9 - i6 * i7)
    c = i3 * (i4 * i8 - i7 * i5)
    d = a - b + c
    l = Label(root, text="The determinant is:", fg="blue")
    l.place(x=20, y=150)
    mylabel = Label(root, text=d, fg="red")
    mylabel.place(x=150, y=150)

    if d != 0:
        m = Label(root, text="The inverse is:", fg="blue").place(x=20, y=170)
        l1 = i5 * i9 - i8 * i6
        l2 = -(i4 * i9 - i7 * i6)
        l3 = i4 * i8 - i7 * i5
        l4 = -(i2 * i9 - i3 * i8)
        l5 = i1 * i9 - i3 * i7
        l6 = -(i1 * i8 - i7 * i2)
        l7 = i2 * i6 - i3 * i5
        l8 = -(i1 * i6 - i3 * i4)
        l9 = i1 * i5 - i2 * i4
        L1 = Label(root, text=Fraction(l1, d)).place(x=20, y=200)
        L2 = Label(root, text=Fraction(l2, d)).place(x=20, y=230)
        L3 = Label(root, text=Fraction(l3, d)).place(x=20, y=260)
        L4 = Label(root, text=Fraction(l4, d)).place(x=50, y=200)
        L5 = Label(root, text=Fraction(l5, d)).place(x=50, y=230)
        L6 = Label(root, text=Fraction(l6, d)).place(x=50, y=260)
        L7 = Label(root, text=Fraction(l7, d)).place(x=80, y=200)
        L8 = Label(root, text=Fraction(l8, d)).place(x=80, y=230)
        L9 = Label(root, text=Fraction(l9, d)).place(x=80, y=260)

    if d == 0:
        L10 = Label(root, text="Inverse is not defined", fg="red").place(x=10, y=230)        

mybutton = Button(root, text="CALCULATE", fg="red", bg="white", command=determinant)
mybutton.place(x=20, y=110)
root.mainloop()