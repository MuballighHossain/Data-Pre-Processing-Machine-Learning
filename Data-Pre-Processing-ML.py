# -*- coding: utf-8 -*-
"""9_19101289_MdMuballighHossainBhuyain.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mH-GlEZgCyBhzQnbGcxsdrBphCaQFz-Z
"""

# Importing the required Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk

# Mounting Drive to the Colab Notebook
from google.colab import drive
drive.mount('/content/drive')

# We will read our CSV file from our Google Drive and store it in a variable called df
df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Melanoma.csv')

#Viewing the shape and structure of our dataset/ counting rows and columns of the data set
df.shape

#Viewing a portion of the dataset to learn more about it
df.head(10)

# Counting the empty columns
df.isna().sum()

df.describe()

# We can see that all of our columns hold value, only anatom_site_general_challenge, sex and age_approx columns have a few null values.
# but that is trivial in comparison to 33126.
# So we are not dropping any columns. 
# However we can sort out the row values

# -------------------  Dropping Null or Empty Values from Row. We do this to improve our training program. ------------------------------------------

# Counting Number of missing values in the 'Sex' Column
print("Null Values : ", df['sex'].isnull().sum())
# Creating a Subset
df_subset = df[df['sex'].notnull()]
# Printing Shape
print("Shape of dataframe before dropping:", df.shape)
# Dropping null values from the row
df = df.dropna(axis = 0, subset = ['sex'])
print("Shape after dropping:", df.shape)

# Counting Number of missing values in the 'anatom_site_general_challenge' Column
print("Null Values : ", df['anatom_site_general_challenge'].isnull().sum())
# Creating a Subset
df_subset = df[df['anatom_site_general_challenge'].notnull()]
# Printing Shape
print("Shape of dataframe before dropping:", df.shape)
# Dropping null values from the row
df = df.dropna(axis = 0, subset = ['anatom_site_general_challenge'])
print("Shape after dropping:", df.shape)

# -------------------  Imputing Values in our dataset. We do this to improve our training program. ------------------------------------------

# Imputing Values in the 'age_approx' column
from sklearn.impute import SimpleImputer
impute = SimpleImputer(missing_values=np.nan, strategy='mean')
impute.fit(df[['age_approx']])
df['age_approx'] = impute.transform(df[['age_approx']])
df.isna().sum() # checking if any column has any empty values

df.head() # To verify whether there is any empty column

# -------------------  Encoding Starts Here ------------------------------------------

# Counting Malignant and Benign Cells
df['benign_malignant'].value_counts()

# Visualizing benign vs malignant
sns.countplot(df['benign_malignant'],label='count')

# Encoding categorical features
from sklearn.preprocessing import LabelEncoder
encode = LabelEncoder()

# Encoding 'benign_malignant'
df.iloc[:,6] = encode.fit_transform(df.iloc[:,6].values)
df.iloc[:,6]

# Encoding 'sex'
df.iloc[:,2] = encode.fit_transform(df.iloc[:,2].values)
df.iloc[:,2]

# Encoding 'diagnosis'
df.iloc[:,5] = encode.fit_transform(df.iloc[:,5].values)
df.iloc[:,5]

# Encoding 'anatom_site_general_challenge'
df.iloc[:,4] = encode.fit_transform(df.iloc[:,4].values)
df.iloc[:,4]

df.head(5) # verifying if our encoding was successful

# Pair Plot 
sns.pairplot(df.iloc[:,2:7], hue='benign_malignant')

# Finding out Correlation between columns
df.iloc[:,2:11].corr()

# Visualizing correlation
sns.heatmap(df.iloc[:,2:11].corr(),annot=True, fmt='.0%')

# -------------------  Splitting Begins Here ------------------------------------------

# Splitting the dataset into independent X and dependent Y
x = df.drop(['diagnosis','image_name','patient_id','patient_code'],axis=1)
y = df['diagnosis']

# Train and Test Split --- > Train : 70%, Test : 30%
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.7, random_state=0)
print("Training dataset shape : ",x_train.shape)
print("Testing dataset shape : ",x_test.shape)
x_train.head()

# -------------------  Scaling Begins Here ------------------------------------------

# Scaling our data in order to remove biasness or deviance - Feature Scaling
# Method - Min Max Scaling Method
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(x_train)

# Transforming
x_train_temp = scaler.transform(x_train)

print("Minimum Values of each feature before being scaled:\n {}".format(x_train.min(axis=0)))
print("Maximum Values of each feature before being scaled:\n {}".format(x_train.max(axis=0)))

print("Minimum Values of each feature before being scaled:\n {}".format(x_train_temp.min(axis=0)))
print("Maximum Values of each feature before being scaled:\n {}".format(x_train_temp.max(axis=0)))