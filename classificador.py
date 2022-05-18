from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from pandas import crosstab
import time
import numpy as np

data = []
target = []
X_train = None
X_test = None
y_train = None
y_test = None
clf = None # Svm


def carregarBase(ldata, ltarget):
    global data
    global target
    
    data = ldata
    target = ltarget

def treinarBase():
    global X_train, X_test, y_train, y_test, clf

    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.25) # 75% treino e 25% teste

    clf = svm.SVC(kernel='linear', C=1, gamma=1) # Classificador

    # Treinar
    tInicial = time.time()
    clf.fit(X_train, y_train)
    tTreino = time.time() - tInicial

    # Classficiar resto da base
    tInicial = time.time()
    y_pred = clf.predict(X_test)
    tClassificacao = time.time() - tInicial
    
    # Obter dados
    accuracy = metrics.accuracy_score(y_test, y_pred)
    confMatrix = confusion_matrix(y_test, y_pred)

    FP = confMatrix.sum(axis=0) - np.diag(confMatrix)
    FN = confMatrix.sum(axis=1) - np.diag(confMatrix)
    TP = np.diag(confMatrix)
    TN = confMatrix.sum() - (FP + FN + TP)
    TPR = TP / (TP + FN)  # Sensibilidade ou hit rate
    TNR = TN / (TN + FP)  # Specificidade
    
    sensibilidade = round(TPR.mean(), 2)
    especificidade = round(TNR.mean(), 2)

    return accuracy, sensibilidade, especificidade, tTreino, tClassificacao, crosstab(y_test, y_pred, rownames=['Real'], colnames=['Predito'], margins=True)

def classificar(ldata):
    return clf.predict([ldata])