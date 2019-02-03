# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 20:49:12 2018

@author: srihari
"""

import matplotlib.pyplot as py
import numpy as np
import pandas as pd

train = pd.read_csv("C:/Users/sriha/Desktop/Kaggle Volcanoes on venus Dataset/train_images.csv",
                    header=None)

train_labels = pd.read_csv("C:/Users/sriha/Desktop/Kaggle Volcanoes on venus Dataset/train_labels.csv")
train_labels = train_labels.iloc[:,0].as_matrix()


# pre-processing
x = np.sum(train,axis=1)
trainNew = train[x > 0]
nonZeroIndices = np.where(x != 0)[0]
train_labels = train_labels[nonZeroIndices]

# Normalizing data between 0 and 1
X_train = trainNew / 255

# Import keras 
import keras
from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()

classifier.add(Dense(output_dim=6,init='uniform',activation='relu',input_dim=12100))
classifier.add(Dense(output_dim=6,init='uniform',activation='relu'))
classifier.add(Dense(output_dim=1,init='uniform',activation='sigmoid'))
classifier.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['accuracy'])
classifier.fit(X_train,train_labels,batch_size=10,nb_epoch=20)

###### testing the model on test dataset

# read test data
test = pd.read_csv("C:/Users/sriha/Desktop/Kaggle Volcanoes on venus Dataset/test_images.csv",
                    header=None)

# pre-process test data
x1 = np.sum(test,axis=1)
testNew = test[x1 > 0]
nonZeroIndices1 = np.where(x1 != 0)[0]

# read test labels
test_labels = pd.read_csv("C:/Users/sriha/Desktop/Kaggle Volcanoes on venus Dataset/test_labels.csv")
test_labels = test_labels.iloc[:,0].as_matrix()
test_labels = test_labels[nonZeroIndices1]

X_test = testNew / 255



# prediction
pred = classifier.predict(X_test)
py.figure()
py.hist(pred)
pred = (pred > 0.2)

# confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(test_labels,pred)

AccuracyPer = (cm.diagonal().sum()/cm.sum())*100
print(AccuracyPer)


