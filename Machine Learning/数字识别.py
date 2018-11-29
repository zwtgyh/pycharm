import numpy as np
import pandas as pd
from keras.utils import np_utils
np.random.seed(10)
from keras.datasets import mnist
#载入数据集
(x_train_image, x_train_label),\
(x_test_image, x_test_label) = mnist.load_data()
#显示训练、检验数据集长度
print('train data=',len(x_train_image))
print('test data=',len(x_test_image))
#训练数据集由image和label组成
print('x_train_image:',x_train_image.shape)
print('x_train_label:',x_train_label.shape)
#定义函数plot显示image
import matplotlib.pyplot as plt
def plot_image(image):
    fig = plt.gcf()
    fig.set_size_inches(2,2)
    plt.imshow(image,cmap='binary')
    plt.show()
#查看第n+1项的图像、标签
plot_image(x_train_image[0])
x_train_label[0]
#自己写一个查看数据图片、标签的函数
def look_data(x):
    print(plot_image(x_train_image[x]))
    print(x_train_label[x])

look_data(200)

#查看多项图像、标签
import matplotlib.pyplot as plt
def plot_images_labels_prediction(images,labels,prediction,idx,num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num>25 :num=25
    for i in range(0, num):
        ax = plt.subplot(5,5,1+i)
        ax.imshow(images[idx], cmap='binary')
        title = "label=" +str (labels[idx])
        if len(prediction)>0:
            title+=",predict=" + str(prediction)
        ax.set_title(title,fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx+=1
    plt.show()

plot_images_labels_prediction(x_train_image,x_train_label,[],0,10)
#原始图像格式
print('x_train_image:',x_train_image.shape)
print('x_train_label:',x_train_label.shape)
#转换数据为一维向量
x_Train = x_train_image.reshape(60000,784).astype('float32')
x_Test = x_test_image.reshape(10000,784).astype('float32')
#查看一维向量的shape
print('x_Train:',x_Train.shape)
print('x_Test:',x_Test.shape)
#查看一维向量的内容
x_train_image[0]
#or
x_Train[0]
#标准化
x_Train_normalize = x_Train/255
x_Test_normlize = x_Test/255
#原始label
x_train_label[:5]
#对label进行One-Hot Encoding转换
x_TrainOneHot = np_utils.to_categorical(x_train_label)
x_TestOneHot = np_utils.to_categorical(x_test_label)
#转换后的label
x_TrainOneHot[:5]