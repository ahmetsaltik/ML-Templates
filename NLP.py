#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: ahmetsaltik
"""

import numpy as np
import pandas as pd

comments = pd.read_csv('Restaurant_Reviews.csv')

import re
import nltk

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

nltk.download('stopwords')
from nltk.corpus import stopwords

#Preprocessing 
compilation = []
for i in range(1000):
    comment = re.sub('[^a-zA-Z]',' ',comments['Review'][i])
    comment = comment.lower()
    comment = comment.split() # or use nltk.word_tokenize(comments)
    comment = [ps.stem(word) for word in comment if not word in set(stopwords.words('english'))]
    comment = ' '.join(comment)
    compilation.append(comment)
    
#Feautre Extraction 
#Bag of Words (BOW)
from sklearn.feature_extraction.text import CountVectorizer  #to create bag of words
cv = CountVectorizer(max_features = 2000)
X = cv.fit_transform(compilation).toarray() # independent variable --> sparce_matrix
y = comments.iloc[:,1].values # dependent variable --> classes
 
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train,y_train)

y_pred = gnb.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)



















