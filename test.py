import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#this is all done on pitching data

df = pd.read_csv("LargeTest.csv")
#just a list of column names that we will use for feature selection didn't include stats like Wins and Loss because that is a result of the other stats
cols = ["RA/G","ERA","G","GS","GF","CG","tSho","cSho","SV","IP","H","R","ER","HR","BB","IBB","SO","HBP","BK","WP","BF","ERA+","FIP","WHIP","H9","HR9","BB9","SO9"]
#normalizing the data
for i in cols:
    df[i] = df[i]/df[i].max()

#logistic regression and Recursive Feature Elemination
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE

X = df[cols]
y = df["post"]

model = LogisticRegression()
#10 as a guess of the number of features
rfe = RFE(model, 10)
rfe = rfe.fit(X, y)
print('Selected features: %s' % list(X.columns[rfe.support_]))
#['RA/G', 'ERA', 'tSho', 'SV', 'R', 'ER', 'IBB', 'SO', 'ERA+', 'H9']

#cross validation with RFE
from sklearn.feature_selection import RFECV
rfecv = RFECV(estimator=LogisticRegression(), step=1, cv=10, scoring='accuracy')
rfecv.fit(X, y)

print("Optimal number of features: %d" % rfecv.n_features_)
print('Selected features: %s' % list(X.columns[rfecv.support_]))
#11 selected features ['RA/G', 'ERA', 'tSho', 'SV', 'R', 'ER', 'IBB', 'SO', 'ERA+', 'WHIP', 'H9']
plt.figure(figsize=(10,6))
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score (nb of correct classifications)")
plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
plt.show()

selected_features = ['RA/G', 'ERA', 'tSho', 'SV', 'R', 'ER', 'IBB', 'SO', 'ERA+', 'WHIP', 'H9']

X = df[selected_features]
plt.subplots(figsize=(8, 5))
sns.heatmap(X.corr(), annot=True, cmap="RdYlGn")
plt.show()
