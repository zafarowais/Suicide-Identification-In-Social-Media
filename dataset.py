import os
from tkinter import *
import tkinter.ttk as ttk
import csv
root = Tk()
root.title("Social")
width = 1366
height = 768
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = 1366
y = 768
root.geometry("1366x768")
root.resizable(0, 0)
label_0 = Label(root, text="Social", width=15, font=("bold", 10))
label_0.place(x=1, y=5)

TableMargin = Frame(root, width=1000)
TableMargin.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)

tree = ttk.Treeview(TableMargin, columns=("textID", "text", "selected_text", "sentiment"), height=400,
                    selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('textID', text="textID", anchor=W)
tree.heading('text', text="text", anchor=W)
tree.heading('selected_text', text="selected_text", anchor=W)
tree.heading('sentiment', text="sentiment", anchor=W)


tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=100)
tree.column('#2', stretch=NO, minwidth=0, width=700)
tree.column('#3', stretch=NO, minwidth=0, width=100)

tree.pack()



with open('Tweets.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        a1 = row['textID']
        a2 = row['text']
        a3 = row['selected_text']
        a4 = row['sentiment']

        tree.insert("", 0, values=(a1, a2, a3, a4))

os.system('python dataset1.py')
root.mainloop()
