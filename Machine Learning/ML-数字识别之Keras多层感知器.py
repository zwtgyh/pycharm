####数据预处理
#导入必要模块
from keras.utils import np_utils
import numpy as np
np.random.seed(10)
#读数据
from keras.datasets import mnist
(x_train_image,y_train_label),(x_test_image,y_test_label) = mnist.load_data()
#转换数据为浮点数
x_Train = x_train_image.reshape(60000,784).astype('float32')
x_Test = x_test_image.reshape(10000,784).astype('float32')
#标准化
x_Train_normalize = x_Train/255
x_Test_normalize = x_Test/255
#One-Hot Encoding转换
y_Train_onehot = np_utils.to_categorical(y_train_label)
y_Test_onehot = np_utils.to_categorical(y_test_label)
####建立模型
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
#输入层与隐藏层
model.add(Dense(units=256,
                input_dim=784,
                kernel_initializer='normal',
                activation='relu'))
#输出层
model.add(Dense(units=10,
                kernel_initializer='normal',
                activation='softmax'))
print(model.summary())
#定义训练模式
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
#开始训练
train_history = model.fit(x=x_Train_normalize,
                          y=y_Train_onehot,
                          validation_split=0.2,        #80%作为训练数据集，20%作为验证数据集
                          epochs=10,                   #训练循环次数
                          batch_size=200,              #每批训练的数据个数
                          verbose=2)                   #显示训练过程
#画图显示训练过程
import matplotlib.pyplot as plt
def show_train_history(train_history,train,validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title('Train History')
    plt.ylabel(train)
    plt.xlabel('Epoch')
    plt.legend(['train','validation'], loc='upper left')
    plt.show()

show_train_history(train_history,'acc','val_acc')  #准确率结果
show_train_history(train_history,'loss','val_loss')  #误差率结果
#用测试数据评估模型准确率
scores = model.evaluate(x_Test_normalize,y_Test_onehot)
print('accuracy=',scores[1])
#进行预测
prediction = model.predict_classes(x_Test)
prediction
#将预测结果显示出来
def plot_images_labels_prediction(images,labels,prediction,idx,num=10):  #默认显示10项
    fig = plt.gcf()
    fig.set_size_inches(12, 14)      #设置显示图像大小
    if num>49 :num=49                #超过49项就显示前49项
    for i in range(0, num):          #画出循环中num项的图像
        ax = plt.subplot(7,7,1+i)    #7*7图像显示
        ax.imshow(images[idx], cmap='binary')
        title = "label=" +str (labels[idx])      #设置标签
        if len(prediction)>0:                    #如果函数中给出预测值
            title+=",predict=" + str(prediction[idx])
        ax.set_title(title,fontsize=10)          #设置图形标题与大小
        ax.set_xticks([])                        #不显示刻度
        ax.set_yticks([])
        idx+=1                                   #读取下一项
    plt.show()
plot_images_labels_prediction(x_test_image,y_test_label,prediction,num=49,idx=340)

#显示混淆矩阵(显示哪些数字预测准确率高，哪些图形容易被混淆)
import pandas as pd
pd.crosstab(y_test_label,prediction,
            rownames=['label'],colnames=['predict'])       #(对角线是预测正确的数字)
df = pd.DataFrame({'label':y_test_label, 'predict':prediction})
df[:10]                                  #显示前十项数据
df[(df.label==5)&(df.predict==3)]       #显示实际上是5却被识别为3的数据
plot_images_labels_prediction(x_test_image,y_test_label,prediction,num=1,idx=6043)

########模型完善
#增加隐藏层从256到1000
model = Sequential()
#输入层与隐藏层(增加到1000)
model.add(Dense(units=1000,
                input_dim=784,
                kernel_initializer='normal',
                activation='relu'))
#输出层
model.add(Dense(units=10,
                kernel_initializer='normal',
                activation='softmax'))
print(model.summary())
#定义训练模式并开始训练
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
train_history = model.fit(x=x_Train_normalize,
                          y=y_Train_onehot,
                          validation_split=0.2,        #80%作为训练数据集，20%作为验证数据集
                          epochs=10,                   #训练循环次数
                          batch_size=200,              #每批训练的数据个数
                          verbose=2)                   #显示训练过程

#########多层感知器加入DropOut功能以防过拟合
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
model = Sequential()
#输入层与隐藏层(增加到1000)
model.add(Dense(units=1000,
                input_dim=784,
                kernel_initializer='normal',
                activation='relu'))
#加入Dropout功能
model.add(Dropout(0.5))
#输出层
model.add(Dense(units=10,
                kernel_initializer='normal',
                activation='softmax'))
print(model.summary())
#定义训练模式并开始训练
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
train_history = model.fit(x=x_Train_normalize,
                          y=y_Train_onehot,
                          validation_split=0.2,        #80%作为训练数据集，20%作为验证数据集
                          epochs=10,                   #训练循环次数
                          batch_size=200,              #每批训练的数据个数
                          verbose=2)                   #显示训练过程

############多层感知器加入两个隐藏层
model = Sequential()
#输入层与隐藏层1
model.add(Dense(units=1000,
                input_dim=784,
                kernel_initializer='normal',
                activation='relu'))
model.add(Dropout(0.5))
#隐藏层2
model.add(Dense(units=1000,
                kernel_initializer='normal',
                activation='relu'))
model.add(Dropout(0.5))
#输出层
model.add(Dense(units=10,
                kernel_initializer='normal',
                activation='softmax'))
print(model.summary())
#定义训练模式并开始训练
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
train_history = model.fit(x=x_Train_normalize,
                          y=y_Train_onehot,
                          validation_split=0.2,        #80%作为训练数据集，20%作为验证数据集
                          epochs=10,                   #训练循环次数
                          batch_size=200,              #每批训练的数据个数
                          verbose=2)                   #显示训练过程