import pandas as pd
import numpy as np
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score

# 加载数据
data = pd.read_csv('chapter_data.csv')
head = data.head()

# 去掉y这一列，将其它数据赋值给X
X = data.drop(['y'], axis=1)

# y赋值
y = data.loc[:, 'y']  # 从所有行中选择'y'这一列赋值给y变量
print(y)
'''
0     1
1     1
2     1
3     0
4     1
5     0
6     0
7     1
8     0
9     0
10    0
'''

# 创建模型实例，模型训练
model = CategoricalNB()
model.fit(X, y)

y_predict_prob = model.predict_proba(X)
print(y_predict_prob)
'''
[[0.48480565 0.51519435]
 [0.31114639 0.68885361]
 [0.3341655  0.6658345 ]
 [0.28647866 0.71352134]
 [0.5009356  0.4990644 ]
 [0.58532423 0.41467577]
 [0.80059811 0.19940189]
 [0.61627001 0.38372999]
 [0.60089784 0.39910216]
 [0.72801439 0.27198561]
 [0.58532423 0.41467577]]
 上面第一列是y=0的概率，第二列是y=1的概率
'''

# 输出根据上面的样本数据X预测的y的数据
y_predict = model.predict(X)
print(y_predict)
'''
[1 1 1 1 0 0 0 0 0 0 0]
这就是上面11个用户购买商品的概率
'''
# 计算模型准确率
accuracy = accuracy_score(y, y_predict)
print(accuracy)  # 0.7272727272727273

# 测试样本数据的预测结果
# X_test = np.array([[0, 0, 0, 1, 1, 0]])
X_test = pd.DataFrame([[0, 0, 0, 1, 1, 0]], columns=["gender", "age", "status", "city", "cost", "device"])
y_test_proba = model.predict_proba(X_test)
print(y_test_proba)
'''
[[0.48480565 0.51519435]]
左边的是0的概率，右边的是1的概率
'''
y_test = model.predict(X_test)
print(y_test)
'''
1
预测结果为1，代表预测用户会购买
'''
