#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:01:34 2020

@author: iiitb
"""

from tkinter import *
import os
import csv

import cv2
import numpy as np



root = Tk()
root.geometry('500x500')
root.title("Login Form")


Username=StringVar()
Password=StringVar()


def login():
    print (Username.get())
    print (Password.get())
    if Username.get()=='admin' and Password.get()=='admin':
          os.system('python train.py')

    

label_0 = Label(root, text="Login form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="User Name",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Username)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Password",width=20,font=("bold", 10))
label_2.place(x=80,y=180)

entry_2 = Entry(root,textvar=Password)
entry_2.place(x=240,y=180)

Button(root, text='Login',width=20,bg='brown',fg='white',command=login).place(x=180,y=330)

root.mainloop()
