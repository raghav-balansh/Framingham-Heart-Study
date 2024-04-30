import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import StackingClassifier
from sklearn.svm import LinearSVC
from sklearn.neural_network import MLPClassifier

import pickle
df = pd.read_csv('CHD_preprocessed.csv')

x = df.drop(columns='TenYearCHD')
y = df['TenYearCHD']

estimators = [
    ('svc', make_pipeline(StandardScaler(),
                          LinearSVC(random_state=42))),
    ('mlp', make_pipeline(StandardScaler(), MLPClassifier(alpha=1, max_iter=100)))

]
clf = StackingClassifier(
    estimators=estimators, final_estimator=LogisticRegression(random_state=42), cv=10, n_jobs=-1, verbose=2
)


X_train, X_test, y_train, y_test = train_test_split(x, y, stratify=y, random_state=42)

clf.fit(X_train, y_train)


pickle.dump(clf, open('model.pickle', 'wb'))
