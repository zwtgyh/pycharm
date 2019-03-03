import random
random.seed(1)
listC = ['加多宝','雪碧','可乐','勇闯天涯','椰子汁']
print(random.choice(listC))
A = ['a','b']
A.append('c')
dictMenu = {'卡布奇洛':32,'摩卡':30,'抹茶蛋糕':28,'布朗尼':26}
sum = 0
for i in dictMenu.values():
    sum += i
print(sum)

dictMenu = {'卡布奇洛':32,'摩卡':30,'抹茶蛋糕':28,'布朗尼':26}
sum = 0
for i in dictMenu.values():
    sum += i
print(sum)


N = input()
print(N[::-1])
a = input()
print(a.lower())


s = input()
print(s.replace('py','python'))

s = input()
ss = s.split(',')
sss = []
for i in ss:
    sss.append(int(i))
print(max(ss))

data = input()
a = data.split(",")
b = []
for i in a:
    b.append(int(i))
print(max(b))

s = input()
print(max(s))

s = "123"
print(True if type(eval(s)) == int else False)

ls = [123,'456',789,'123',456,'789']
s = 0
for item in ls:
    if type(item) == type(123):
        s += item
print(s)

while True:
    s = input('请输入任意字符: ')
    if s in ['y','Y']:
        break


while True:
    try:
        s = input()
        print(100/eval(s))
        break
    except:
        ''

while True:
    s = input()
    try:
        print(100/eval(s))
        break
    except:
        ""

s = input()
if s == 'a':
    print("111")
if s == 'b':
    print("222")

def psum(a,b=10):
    return a**2+b**2 , a+b
a = eval(input())
print(psum(a))

def psum(a, b=10):
   return (a**2 + b**2), (a+b)

a=eval(input())
print(psum(a))

import jieba
txt = "中华人民共和国教育部考试中心委托专家定制了全国计算机等级考试二级程序设计考试大纲"
ls = jieba.lcut(txt,cut_all=True)
print(ls)

ls = [123,'456',789,'123',465,'789']
ls.insert(3,'012')
print(ls)

d = {123:"123", 456:"456", 789:"789"}

s = input("请输入一个汉字： ")
print("汉字\"{}\"的Unicode编码是: {}".format(s,ord(s)))

def gcd(a,b):
    if a < b :
        a,b = b,a
    while a % b != 0:
        c = a % b
        a = b
        b = c
    return b

def mean(numlist):
    s = 0
    for num in numlist:
        s += num
    return s/len(numlist)

ls = eval(input("请输入一个列表: "))
print("平均值为: ",mean(ls))

ls = list(eval(input()))
for i in range(len(ls)):
    ls[i] = ls[i].capitalize()
print(ls)

def f(n):
    sum = 0
    if n/2!=0:
        for i in range(1,n+1,2):
            sum += 1/i
    else:
        for i in range(2,n+1,2):
            sum += 1/i
    return sum
n = int(eval(input()))
print("{:.2f}".format(f(n)))

fruits = {"apple":10,"mango":12,"durian":20,"banana":5}
m = 'apple'
for key in fruits.keys():
    if fruits[m] < fruits[key]:
        m = key
print("{}:{}".format(m,fruits[m]))

a = input("请输入填充符号: ")
s = 'PYTHON'
print("{:{}^30}".format(s,a))

m = input("请输入对齐模式：")
s = "PYTHON"
if  m =="右":
    m = ">"
elif  m =="中":
    m = "^"
else:
    m = "<"
print("{:*{}30}".format(s,m)

m = input("请输入对齐模式：")
s = "PYTHON"
if  m =="右":
    m = ">"
if  m =="中":
    m = "^"
if  m =="左":
    m = "<"
print("{:*{}30}".format(s,m)

s = input()
print("{:^30.10}".format(s))
print("{:>30.3f}".format(eval(s)))

n = input()
print("{:^30X}".format(eval(n)))

s = input()
count = 0
for i in s:
    if 0x4e00 <= ord(i) <= 0x9fa5 :\
    count+=1
print(count)

n = input()
for i in range(eval(n),eval(n)+10):
    print(chr(i) , end=' ')


n = input("请输入一个整数：")
for i in range(10):
    print(chr(eval(n)+i))