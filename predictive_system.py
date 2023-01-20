import numpy as np
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from Metadata import getmetadata

loaded_model = pickle(
    open('trained_model.sav', 'rb'))

df = pd.read_csv('data.csv')
scaler = MinMaxScaler()
lookup_genre_name = dict(zip(df.class_label.unique(), df.class_name.unique()))
input = getmetadata("sample1.wav")

d1 = np.array(input)
data1 = scaler.transform([d1])
model = loaded_model.predict(data1)
print(lookup_genre_name[model[0]])
