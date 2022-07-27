from tkinter import *
from mysql import-connector
from tkinter import messagebox
y=0

top = Tk()
top.geometry("600x600")
registrationform = Label(top, text="Registrationform").place(x=100, y=50)
SrNo = Label(top, text="SrNo").place(x=30, y=90)
e1 = Entry(top, width=50).place(x=60, y=90)

Name = Label(top, text="Name").place(x=30, y=130)
e2 = Entry(top, width=50).place(x=60, y=130)

Rollno = Label(top, text="Rollno").place(x=30, y=170)
e3 = Entry(top, width=50).place(x=60, y=170)

AddressNo = Label(top, text="AddressNo").place(x=30, y=210)
e4 = Entry(top, width=50).place(x=60, y=210)

branch = Label(top, text="branch").place(x=30, y=250)
menu= StringVar()
menu.set("Select Any stream")

#Create a dropdown Menu
drop= OptionMenu(top, menu,"electronics", "CSe","civil","production","mining","it").place(x=100,y=250)

gender = Label(top, text="gender").place(x=30, y=400)
var=IntVar
r1=Radiobutton(top,text="male",variable=var,value=1).place(x=100,y=400)
r2=Radiobutton(top,text="female",variable=var,value=1).place(x=100,y=440)
submit = Button(top, text="submit").place(x=30, y=570)
top.mainloop()
