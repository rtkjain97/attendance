#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 20:49:53 2020

@author: iiitb
"""
import tkinter as tk
import datetime

from tkinter import *
import os
import csv
import time
import pandas as pd
from tkinter import messagebox
from PIL import Image

import numpy as np
from tkinter import messagebox
import cv2
import recognize

root = Tk()
root.geometry('500x500')
root.title("ADMIN")

def clear1():
    txt.delete(0, 'end')    
    res = ""
    message.configure(text= res)

def clear2():
    txt2.delete(0, 'end')    
    res = ""
    message.configure(text= res)    
    

def getImagesAndLabels(path):
    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # print(imagePaths)

    # create empth face list
    faces = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids


def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Image Trained"
    #clear1();
   # clear2();
    #Smessage.configure(text= res)
    tk.messagebox.showinfo('Completed','Your model has been trained successfully!!')
    print("dddd")
    
    




def TrackImages():
       recognize.TrackImages()

Button(root, text='Train IMages',width=20,bg='brown',fg='white',command=TrainImages).place(x=180,y=200)
Button(root, text='Recognize',width=20,bg='brown',fg='white',command=TrackImages).place(x=180,y=230)

root.mainloop()