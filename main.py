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
