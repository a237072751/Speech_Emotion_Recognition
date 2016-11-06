import pandas as pd

from sklearn.cross_validation import cross_val_score
import random
from sklearn.cross_validation import cross_val_predict	
from sklearn.cross_validation import cross_val_score
import matplotlib.pyplot as plt
from sklearn.multiclass import OutputCodeClassifier

from sklearn.metrics import classification_report
#data processing
feature = pd.read_csv("/home/chang/my/speech/data/feature.csv")
data = feature.values
random.shuffle(data)
X = data[:,1:]
y = data[:,0]
#train
from sklearn.multiclass import OneVsOneClassifier
from sklearn.svm import LinearSVC
clf = OneVsOneClassifier(LinearSVC(random_state=0))#fit(X,y)
#y_pred = clf.predict(X)
#print(classification_report(y, y_pred))



#pridict
scores = cross_val_score(clf, X, y, cv=10)
print scores
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))


