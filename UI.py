#import module from tkinter for UI
from tkinter import *
import os
from datetime import datetime;
#creating instance of TK
root=Tk()

root.configure(background="#aed6dc")



def function1():
    
    os.system("model2.py")
    
def function2():
    
    os.system("model1.py")

def function3():

    os.system("members.py")

 
def function6():

    root.destroy()

#stting title for the window
root.title("Modelling And Simulation Project")

#creating a text label
Label(root, text="Group 3's Modelling and Simulation Project",font=("verdanna",20),fg="#4a536b",bg="#aed6dc",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Label(root, text="Please Click one of the buttons below to run the program",font=("verdanna",15),fg="#4a536b",bg="#aed6dc",height=2).grid(row=2,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
#creating first button
Button(root,text="Problem Statement",font=("verdanna",20),bg="#316879",fg='#aed6dc',command=function1).grid(row=4,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Realistic Simulation",font=("verdanna",20),bg="#316879",fg='#aed6dc',command=function2).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Group Memebers",font=('verdanna',20),bg="#316879",fg="#aed6dc",command=function3).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('verdanna',20),bg="#316879",fg="#f47a60",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
