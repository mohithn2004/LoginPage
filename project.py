from tkinter import *
from tkinter import messagebox
from tkinter import messagebox as MsgBoxVap
import tkinter.messagebox as MsgBoxVap
from PIL import Image, ImageTk

Sup = Tk()
text= StringVar()
Sup.title("Login Page")
Sup.geometry("1265x900")
Sup.configure(background='#F2EAD3')


label1 = Label(Sup, text="Sign In",bg="#F2EAD3", fg="#000",font=("Helvetica 18 bold"),borderwidth="0px").place(x=615, y=115)
label2 = Label(Sup, text="Hey, Enter your details to login to your account",bg="#F2EAD3", fg="#000",font=("Roboto",15),borderwidth="0px").place(x=475, y=175)

label3 = Label(Sup, text="Username :",bg="#F2EAD3", fg="#000",font=("Roboto",15),borderwidth="0px")
label3 = label3.place(x=475, y=275)
NamIptTxtBox = Entry(Sup,width=60)
NamIptTxtBox.place(x=475,y=315)

label4 = Label(Sup, text="Password :",bg="#F2EAD3", fg="#000",font=("Roboto",15),borderwidth="0px")
label4 = label4.place(x=475, y=400)
NamPwdTxtBox = Entry(Sup, show="*", width=60)
NamPwdTxtBox.place(x=475, y=435)

def NamBtnKlkFnc():
	MsgBoxVap.showinfo("Log in console","Logged in successfully")

Button(Sup, text="Submit", width=30, command=NamBtnKlkFnc, bg="#AED6B3").place(x=550, y=535)

image = Image.open("Untitled (2)-1.png")
resize_image = image.resize((300, 300))
img = ImageTk.PhotoImage(resize_image)
Label(Sup, image=img).place(x=875, y=235)

Sup.mainloop()