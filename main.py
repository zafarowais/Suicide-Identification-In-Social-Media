from tkinter import *
from PIL import ImageTk, Image

import os
root = Tk()
root.geometry('1366x768')
root.title("Social")

canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back.png')
photo = ImageTk.PhotoImage(img)
canv.create_image(1,1, anchor=NW, image=photo)
def readdataset():
    os.system('python dataset.py')
def preprocessing():
    os.system('python preprocessing.py')

def clf():
        os.system('python classification.py')


def det():
    os.system('python detect.py')
Button(root, text='Load Dataset', width=15,height=1, bg='red', fg='white',  font=("bold", 10),command=readdataset).place(x=750, y=400)
Button(root, text='Preprocessing', width=15,height=1, bg='red', fg='white',  font=("bold", 10),command=preprocessing).place(x=880, y=400)
Button(root, text='Classification', width=15, height=1,bg='red', fg='white',  font=("bold", 10),command=clf).place(x=1010, y=400)

Button(root, text='Detection', height=1,width=15, bg='red', fg='white',command=det,  font=("bold", 10)).place(x=1140, y=400)

root.mainloop()
