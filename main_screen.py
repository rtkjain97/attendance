#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 19:49:36 2020

@author: iiitb
"""

from tkinter import *

root = Tk()
root.geometry('500x500')

def login():
    os.system("python login.py")   


def register(): 
    os.system("python reg.py")   
# create a Form label 
Label(text="Choose Login Or Register", bg="blue", width="300", height="2", font=("Calibri", 13)).pack() 
Label(text="").pack() 

# create Login Button 
Button(root, text='Login',width=20,bg='brown',fg='white',command=login).place(x=180,y=200)

# create a register button
Button(root, text='Register',width=20,bg='brown',fg='white',command=register).place(x=180,y=230)

 
root.mainloop()
