from tkinter import messagebox

import matplotlib.pyplot as plt
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
data = pd.read_csv('Tweets.csv')

data.isnull().sum()
print("===================================")
print("Preprocess data")
print("===================================")
print("null Data=",data.isnull().sum())


X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.05, random_state=0)
print("------------------------")
print("X_Train Data")
print("------------------------")
print(X_train)
print("------------------------")
print("y_Train Data")
print("------------------------")
print(y_train)
print("------------------------")
messagebox.showinfo("Social","Total Tweets: 26106 and 3 attributes, 1 Null Data present in text and selected_text column")