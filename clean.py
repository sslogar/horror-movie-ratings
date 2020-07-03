import pandas as pd
import numpy as np
import os.path
from sklearn.preprocessing import LabelEncoder

filename = 'movie_ratings_edit.csv'

if os.path.isfile(filename):
    movieRaw = pd.read_csv(filename, header=0, index_col=0)
else:
    print("File not in directory")

movieRaw = movieRaw.rename(columns={'Internet Movie Database': 'imdb', 'Rotten Tomatoes': 'rotten' })

movieRaw['rotten'] = movieRaw['rotten'].str.strip('%')
movieRaw['imdb'] = movieRaw['imdb'].str.slice(stop=3)
movieRaw['Metacritic'] = movieRaw['Metacritic'].str.slice(stop=2)

movieRaw.drop('year', axis=1, inplace=True)
movieRaw = pd.get_dummies(movieRaw, columns=['genre'])

le=LabelEncoder()
le.fit(movieRaw['Reddit'])
movieRaw['Reddit'] = le.transform(movieRaw['Reddit'])

objType = list(movieRaw.select_dtypes(include='object').columns)
movieRaw[objType] = movieRaw[objType].astype('float')

movieRaw['meanRating'] = movieRaw[['StephenRating', 'DannyRating']].mean(axis=1)
print(movieRaw[['StephenRating', 'DannyRating']].corr()) #r = 0.891
# print(movieRaw.head(5))

movieRaw = movieRaw.fillna(-1000)

movieRaw.to_csv('movie_ratings_clean.csv')
