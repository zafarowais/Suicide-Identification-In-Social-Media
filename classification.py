import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os

from matplotlib import pyplot as plt

df = pd.read_csv('Tweets.csv', header=0)
df.head()
np.sum(df.isnull())
df['sentiment'].unique()
import seaborn as sns
sns.countplot(x='sentiment', data=df)
plt.xlabel('0:Neutral 1:Suicidal 2: NonSuicidal')
df.isnull().values.any() # checking any null values

df = df.dropna() # drop nan values
df = df.reset_index(drop = True)
df.tail()
X=df['selected_text']
y=df['sentiment']
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
y=le.fit_transform(y)
train_sentences,test_sentences,train_labels,test_labels=train_test_split(X,y,test_size=0.2,random_state=42)
print(f'Total training samples :{train_sentences.shape}')
print("\n")
print(f'Total training labels {train_labels.shape}')
print("\n")
print(f'Total test samples:{test_sentences.shape}')
print("\n")
print(f'Total test labels {test_labels.shape}')

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

model = Pipeline([
    ('vect', CountVectorizer()),  # use CountVectorizer to convert text to numeric features
    ('clf', MultinomialNB())  # use Multinomial Naive Bayes classifier for classification
])
model.fit(train_sentences, train_labels)
accuracy=model.score(test_sentences,test_labels)
print(f'NB model_accuracy:{accuracy}')

model_preds=model.predict(test_sentences)
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, classification_report


def calculate_results(y_true, y_pred):
    model_accuracy = accuracy_score(y_true, y_pred) * 100
    model_precision, model_recall, model_f1, _ = precision_recall_fscore_support(y_true, y_pred, average="weighted")
    model_results = {"accuracy": model_accuracy,
                  "precision": model_precision,
                  "recall": model_recall,
                  "f1": model_f1}
    print(classification_report(y_true, y_pred))
    return model_results
calculate_results(y_true=test_labels,y_pred=model_preds)



plt.show()