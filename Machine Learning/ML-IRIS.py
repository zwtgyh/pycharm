import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
scikit_iris = datasets.load_iris()
iris = pd.DataFrame(
data=np.c_[scikit_iris['data'], scikit_iris['target']],
    columns=np.append(scikit_iris.feature_names, ['y']))
iris.head(2)
iris.isnull().sum()   #检查数据是否有缺失
iris.groupby('y').count()  #观察样本中按类别数量是否均衡
x = iris[scikit_iris.feature_names]
y = iris['y']
#选择model
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
#fit x和y
knn.fit(x,y)
#预测数据
knn.predict([[3,2,2,5]])



#下面是分割数据集的学习、验证过程
from sklearn.model_selection import train_test_split
from sklearn import metrics
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=4)
knn = KNeighborsClassifier(n_neighbors=15)
knn.fit(x_train, y_train)
y_pred_on_train = knn.predict(x_train)
y_pred_on_test = knn.predict(x_test)
print ('accuracy: {}'.format(metrics.accuracy_score(y_test, y_pred_on_test)) )