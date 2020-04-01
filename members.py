#import module from tkinter for UI
from tkinter import *
import os
from datetime import datetime;
#creating instance of TK
root=Tk()

root.configure(background="#aed6dc")


root.title("Group Memebers")

#creating a text label
Label(root, text="Group 3's Members",font=("verdanna",20),fg="#4a536b",bg="#aed6dc",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Label(root, text="1. Ayeni Bolaji Hephzibah 16/1336  Class Number: 21",font=("verdanna",15),fg="#4a536b",bg="#aed6dc",height=2).grid(row=2,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Label(root, text="2. Borisade Mojisola Agatha 16/1813 Class Number: 29",font=("verdanna",15),fg="#4a536b",bg="#aed6dc",height=2).grid(row=4,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Label(root, text="3. Ishola Taofeek Oluwatobi 17/2037  Class Number: 64",font=("verdanna",15),fg="#4a536b",bg="#aed6dc",height=2).grid(row=6,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Label(root, text="4. Ajala Mofiyinfoluwa  16/0812  Class Number: 13",font=("verdanna",15),fg="#4a536b",bg="#aed6dc",height=2).grid(row=8,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Label(root, text="5. Chimaroke Marvellous 17/0090  Class Number: 30",font=("verdanna",15),fg="#4a536b",bg="#aed6dc",height=2).grid(row=10,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

root.mainloop()
