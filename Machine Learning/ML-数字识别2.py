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

P77  7.5

