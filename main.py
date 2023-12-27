import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('heart.csv')
data.columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal','num']

data.info()
des = data.describe().T

#Checking for missing value
missing_values = data.isna().sum()

#Checking if there is a '?' present in the dataset
is_question_mark_present = data.eq('?').any().any()

occurrences = (data == '?').sum() #Sum of '?' occurrences
prec = (1 - occurrences/len(data.iloc[:,1]))*100 #Percentage of non-null values

data.replace('?', np.nan, inplace=True) #inplace=True ensures that the modification is applied to the original dataset

for i in range(3, 13):
    data.iloc[:,i]=data.iloc[:,i].astype(float) #Converting the data types to float

#Replacing the NaN values with mean or median values
data['trestbps'].fillna(data['trestbps'].mean(), inplace=True)
data['oldpeak'].fillna(data['oldpeak'].median(), inplace=True)
data['thalach'].fillna(data['thalach'].mean(), inplace=True)

#Dropping the rows with NaN values
data.dropna(subset=['fbs'], inplace=True)
data.dropna(subset=['exang'], inplace=True)
data.dropna(subset=['restecg'], inplace=True)

data.reset_index(drop=True) #Resetting the indices

data['chol'].replace(0, np.nan, inplace=True)
data['chol'].fillna(data['chol'].median(), inplace=True)

classes = data.iloc[:, data.shape[1]-1] 
value = np.unique(classes)

for u in value:
    p = sum(classes == u)/len(classes)
    print('Appearance of class', str(u), 'in [%]', p*100) #Printing the percent of healthy and ill patients
