import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#This is basically divided into 2 parts: 1- us selecting what features we want to use 2- us making the model 

df = pd.read_csv("LargePitchingBatting.csv")
#just a list of column names that we will use for feature selection didn't include stats like Wins and Loss because that is a result of the other stats
cols = ["RA/G","ERA","G","GS","GF","CG","tSho","cSho","SV","IP","H","R","ER","BB","IBB","SO","HBP","BK","WP","BF","ERA+","FIP","WHIP","H9","HR9","BB9","SO9","R/G","R","H","2B","3B","HR","RBI","SB","CS","BB","SO","BA","OBP","SLG","OPS","OPS+","TB","GDP","HBP","SH","SF","IBB","LOB"]
cols = list(dict.fromkeys(cols))
#normalizing the data
for i in cols:
    df[i] = df[i]/df[i].max()

#1

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
#['RA/G', 'ERA', 'SV', 'R', 'ER', 'ERA+', 'R/G', 'R', 'RBI', 'OPS+']

from sklearn.feature_selection import RFECV
rfecv = RFECV(estimator=LogisticRegression(), step=1, cv=10, scoring='accuracy')
rfecv.fit(X, y)

print("Optimal number of features: %d" % rfecv.n_features_)
print('Selected features: %s' % list(X.columns[rfecv.support_]))
#22 selected features
plt.figure(figsize=(10,6))
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score (nb of correct classifications)")
plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
plt.show()

#['RA/G', 'ERA', 'tSho', 'SV', 'R', 'ER', 'BB', 'IBB', 'ERA+', 'FIP', 'WHIP', 'H9', 'BB9', 'R/G', '2B', 'RBI', 'OBP', 'SLG', 'OPS', 'OPS+', 'TB', 'SF']
#removing non-selected features
selected_features = list(X.columns[rfecv.support_])
bad_features = [x for x in cols if x not in selected_features]

for i in bad_features:
    df = df.drop(i,axis=1)

X = df[selected_features]
y = df['post']

#2

from sklearn.model_selection import train_test_split

#Just getting x & y data to train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

logreg = LogisticRegression()

logreg.fit(X_train,y_train)

y_pred=logreg.predict(X_test)

#making a confusion matrix
from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print("Confusion matrix:",cnf_matrix)
#[[58  1]
# [ 5 19]]

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
#0.927
#Really high accuracy which shows the model is working
print("Precision:",metrics.precision_score(y_test, y_pred))
#0.95
print("Recall:",metrics.recall_score(y_test, y_pred))
#0.7916666666666666
#Single test case Washington Nationals 2019

wsn_X = X.iloc[29]
wsn_y = y.iloc[29]

#wsn_X = wsn_X.reshape(1,-1)
tmp = np.array(wsn_X).reshape(1,-1)
wsn_pred = logreg.predict(tmp)
print("Did the Nationals make the playoffs in 2019?",wsn_y)
#[1]
print("Did the model think the Nationals made the playoffs in 2019?",wsn_pred[0])
#[1]
#Braves 2019

atl_X = X.iloc[29]
atl_y = y.iloc[29]
tmp = np.array(atl_X).reshape(1,-1)
atl_pred = logreg.predict(tmp)
print("Did the Braves make the playoffs in 2019?",atl_y)
print("Did the model think the Braves made the playoffs in 2019?",atl_pred[0])

atl_X = X.iloc[61]
atl_y = y.iloc[61]
tmp = np.array(atl_X).reshape(1,-1)
atl_pred = logreg.predict(tmp)
print("Did the Braves make the playoffs in 2017?",atl_y)
print("Did the model think the Braves made the playoffs in 2017?",atl_pred[0])
#returns 1 which is the correct value