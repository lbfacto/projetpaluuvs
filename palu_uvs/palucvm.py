# -*- coding: utf-8 -*-
"""paludismCNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_XIJZwDm7X_K6gVZbOwCsOSvHoEDe2xQ
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.datasets
from sklearn.model_selection import train_test_split

df=pd.read_excel("/content/drive/MyDrive/palu/palucleaner.xlsx")

print(df)



df=df.drop(['ID','Sexe', 'Type_Hb', 'Gpe_ABO', 'Rhesus'], axis=1)

conditionlist=[(df['ratio']>2),
              (df['ratio']<=2)]
diagnostic = ['0', '1']
df['Resultat'] = np.select(conditionlist, diagnostic)

df

df

features = ['Age', 'ratio', 'G6PD', 'EP_6M_AVT', 'AcPf_6M_AVT', 'EP_1AN_AVT',
            'AcPf_1AN_AVT', 'EP_6M_APR', 'AcPf_6M_APR', 'EP_1AN_APR','AcPf_1AN_APR']
target = ['Resultat']

for attr in ['mean', 'ste', 'largest']:
  for feature in features:
    target.append(feature + "_" + attr)





df['EP_6M_AVT'] = pd.to_numeric(df['EP_6M_AVT'], downcast='float')
df['EP_1AN_APR'] = pd.to_numeric(df['EP_1AN_APR'], downcast='float')
df['AcPf_6M_AVT'] = pd.to_numeric(df['AcPf_6M_AVT'], downcast='float')
df['AcPf_1AN_AVT'] = pd.to_numeric(df['AcPf_1AN_AVT'], downcast='float')
df['EP_6M_APR'] = pd.to_numeric(df['EP_6M_APR'], downcast='float')
df['AcPf_1AN_APR'] = pd.to_numeric(df['AcPf_1AN_APR'], downcast='float')
df['EP_1AN_AVT'] = pd.to_numeric(df['EP_1AN_AVT'], downcast='float')
df['AcPf_6M_APR'] = pd.to_numeric(df['AcPf_6M_APR'], downcast='float')
df['Age'] = pd.to_numeric(df['Age'], downcast='float')
df['ratio'] = pd.to_numeric(df['ratio'], downcast='float')
df['G6PD'] = pd.to_numeric(df['G6PD'], downcast='float')

df['Resultat'] = df['Resultat'].astype(str).astype(int)

df.info()

df.tail()

df.isnull().sum()

df.describe()

df['Resultat'].value_counts()



"""0 -----> **Repond a l'antigene Positif au palu**

1 -----> **Ne repond pas a l'antigene Negatif au palu**
"""



df.shape

"""**Input shape 12**"""

from pandas.io.formats.info import DataFrameInfo
df.groupby('Resultat').mean()

X = df.drop(columns='Resultat', axis=1)
Y = df['Resultat']

print(X)

print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_std = scaler.fit_transform(X_train)

X_test_std = scaler.transform(X_test)

# importing tensorflow and Keras
import tensorflow as tf
tf.random.set_seed(3)
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout

model = keras.Sequential([
                          keras.layers.Flatten(input_shape=(11,)),
                          keras.layers.Dense(20, activation='relu'),
                          keras.layers.Dense(4),
                          keras.layers.Dense(2, activation='sigmoid')
])

# compiling the Neural Network

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# training the Meural Network

history = model.fit(X_train_std, Y_train, validation_split=0.1, epochs=50)

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])

plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')

plt.legend(['training data', 'validation data'], loc = 'lower right')

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])

plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')

plt.legend(['training data', 'validation data'], loc = 'upper right')

loss, accuracy = model.evaluate(X_test_std, Y_test)
print(accuracy)

print(X_test_std.shape)
print(X_test_std[0])

Y_pred = model.predict(X_test_std)

print(Y_pred.shape)
print(Y_pred[0])

print(X_test_std)

print(Y_pred)

"""**model.predict() donne la probabilité de prédiction de chaque classe pour ce point de données.**"""

#  argmax function

my_list = [0.25, 0.56]

index_of_max_value = np.argmax(my_list)
print(my_list)
print(index_of_max_value)

Y_pred_labels = [np.argmax(i) for i in Y_pred]
print(Y_pred_labels)

input_data = (5,3,5.1,0,0,1,1,1,0,1,0)
# change the input_data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the numpy array as we are predicting for one data point
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardizing the input data
input_data_std = scaler.transform(input_data_reshaped)

prediction = model.predict(input_data_std)
print(prediction)

prediction_label = [np.argmax(prediction)]
print(prediction_label)

if(prediction_label[0] == 0):
  print('Antigene positif au PALU')

else:
  print('Antigene NEGATIF au PALU')

input_data = ()

import pickle

filename = 'streamlit_model.pkl'
pickle.dump(model, open(filename, 'wb'))

pickle.dump(model, open('streamlit_model.pkl', 'wb'))

import keras
import tensorflow as tf





loaded_model = pickle.load(open('streamlit_model.sav', 'rb'))

input_data = (5,3,5.1,0,0,1,1,1,0,1,0)
# change the input_data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the numpy array as we are predicting for one data point
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardizing the input data
input_data_std = scaler.transform(input_data_reshaped)

prediction = model.predict(input_data_std)
print(prediction)

prediction_label = [np.argmax(prediction)]
print(prediction_label)

if(prediction_label[0] == 0):
  print('Antigene positif au PALU')

else:
  print('Antigene NEGATIF au PALU')




