import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV
from joblib import dump
import os.path

filename = 'movie_ratings_clean.csv'

if os.path.isfile(filename):
    train = pd.read_csv(filename, header=0, index_col=0)
else:
    print("File not in directory")

X=train.drop(['StephenRating', 'DannyRating', 'meanRating', 'liked'], axis=1)
# X=train.drop(['StephenRating', 'DannyRating', 'meanRating', 'liked'], axis=1)
# y=train['liked']
y=train['meanRating']

parameters={
    'n_estimators': [int(x) for x in np.linspace(10, 150, num=15)],
    'max_depth': [int(x) for x in np.linspace(5, 100, num=20)],
}

#
rf = RandomForestRegressor(criterion='mse', max_features='sqrt')
# clf = RandomForestClassifier(n_estimators=50, max_features='sqrt')
gs = GridSearchCV(estimator=rf, param_grid=parameters, scoring='neg_mean_absolute_error', n_jobs=-1, cv=10)
# scores = cross_val_score(rf, X, y, cv=10, scoring='neg_mean_absolute_error', n_jobs=-1)
# scores = cross_val_score(clf, X, y, cv=10, scoring='accuracy', n_jobs=-1)
gs.fit(X,y)

print('Best score:', gs.best_score_)
print('Best parameters:', gs.best_params_)

dump(gs, 'gridsearchreg.joblib') 
