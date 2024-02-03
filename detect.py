
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import re
import nltk
from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import os
root = Tk()
root.geometry('1366x768')
root.title("Social")

S=StringVar()
R=StringVar()
def back():
    root.destroy()
def find():
    stemmer = nltk.SnowballStemmer("english")
    from nltk.corpus import stopwords
    import string
    stopword = set(stopwords.words('english'))
    data = pd.read_csv("Tweets.csv", encoding='cp1252')
    print(data.head())
    data["labels"] = data["sentiment"].map({0: "neutral",
                                        1: "Suicidal",
                                           2: "NonSuicidal"  })
    print(data.head())
    data = data[["text", "labels"]]

    def clean(text):
        text = str(text).lower()
        text = re.sub('\[.*?\]', '', text)
        text = re.sub('https?://\S+|www\.\S+', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\w*\d\w*', '', text)
        text = [word for word in text.split(' ') if word not in stopword]
        text = " ".join(text)
        text = [stemmer.stem(word) for word in text.split(' ')]
        text = " ".join(text)
        return text


    data["text"] = data["text"].apply(clean)



    x = np.array(data["text"])
    y = np.array(data["labels"])

    cv = CountVectorizer()
    X = cv.fit_transform(x)  # Fit the Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    sample = S.get()
    data = cv.transform([sample]).toarray()
    print(clf.predict(data))
    R.set(clf.predict(data))

canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back.png')
photo = ImageTk.PhotoImage(img)
canv.create_image(1,1, anchor=NW, image=photo)

l1=Label(root,text="Enter Text", font=("BOLD",12))
l1.place(x=250,y=350)
t1=Entry(root,textvar=S,width=50, font=("BOLD",12))
t1.place(x=400,y=350)
t2=Entry(root,textvar=R,width=50, font=("BOLD",12))
t2.place(x=400,y=400)

Button(root, text='Find', width=15, height=1,bg='yellow', fg='black',font=('BOLD',12),command=find).place(x=800, y=450)
Button(root, text='Cancel', width=15, height=1,bg='yellow', fg='black',font=('BOLD',12),command=back).place(x=950, y=450)

root.mainloop()
