import tkinter as tk

from tkinter import *
import os
import csv
import sqlite3
import cv2
import numpy as np
from tkinter import messagebox



root = Tk()
root.geometry('500x500')
root.title("Registration Form")


Fullname=StringVar()
Id=IntVar()





def database():
   name1=Fullname.get()
   id=Id.get()
   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Id TEXT)')
   cursor.execute('INSERT INTO Student (FullName,Id) VALUES(?,?)',(name1,id))
   conn.commit()
   tk.messagebox.showinfo('Completed','Data Stored Succesfully')

   
   
             
label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="ID",width=20,font=("bold", 10))
label_2.place(x=80,y=180)

entry_2 = Entry(root,textvar=Id)
entry_2.place(x=240,y=180)





def TakeImages():        
            print(Id.get())
            print(Fullname.get())
            cam = cv2.VideoCapture(0)
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector=cv2.CascadeClassifier(harcascadePath)
            sampleNum=0
            while(True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                    #incrementing sample number 
                    sampleNum=sampleNum+1
                    #saving the captured face in the dataset folder TrainingImage
                    #cv2.imwrite("TrainingImage "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                    cv2.imwrite("TrainingImage" + os.sep  +Fullname.get()+"."+str(Id.get())+"."+str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                    #display the frame
                    cv2.imshow('frame',img)
                    #display the frame
                #cv2.imshow('frame',img)
                #wait for 100 miliseconds 
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                # break if the sample number is morethan 100
                elif sampleNum>60:
                    break
            cam.release()
            cv2.destroyAllWindows() 
            row = [Id.get() , Fullname.get()]
            with open("StudentDetails"+os.sep+"StudentDetails.csv", 'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
  
   


Button(root, text='Capture',width=20,bg='brown',fg='white',command=TakeImages).place(x=180,y=330)


Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=380)


root.mainloop()























