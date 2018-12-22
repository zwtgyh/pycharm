#数据预处理
from keras.datasets import mnist
from keras.utils import np_utils
import numpy as np
np.random.seed(10)
(x_Train, y_Train), (x_Test, y_Test) = mnist.load_data()  #读数据
x_Train4D = x_Train.reshape(x_Train.shape[0],28,28,1).astype('float32') #转换为4维矩阵
x_Test4D = x_Test.reshape(x_Test.shape[0],28,28,1).astype('float32')
x_Train4D_normalize = x_Train4D / 255  #标准化
x_Test4D_normalize = x_Test4D / 255
y_TrainOneHot = np_utils.to_categorical(y_Train) #One-Hot encoding 转换
y_TestOneHot = np_utils.to_categorical(y_Test)
#建模型
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPooling2D
model = Sequential()
model.add(Conv2D(filters=16,                    #卷积层1
                 kernel_size=(5,5),
                 padding='same',
                 input_shape=(28,28,1),
                 activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))   #池化层1
model.add(Conv2D(filters=36,                    #卷积层2
                 kernel_size=(5,5),
                 padding='same',
                 activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))   #池化层2
model.add(Dropout(0.25))   #每次训练迭代，随机放弃25%的神经元，避免过拟合
model.add(Flatten()) #平坦层
model.add(Dense(128, activation=('relu')) #隐藏层
model.add(Dropout(0.5))
model.add(Dense(10,activation='softmax')) #输出层
print(model.summary())
model.compile(loss='categorical_crossentropy', #定义训练方式
              optimizer='adam',
              metrics=['accuracy'])
train_history = model.fit(x=x_Train4D_normalize, #开始训练
                          y=y_TrainOneHot,
                          validation_split=0.2,
                          epochs=10,
                          batch_size=300,
                          verbose=2)
show_train_history(train_history,'acc','val_acc')