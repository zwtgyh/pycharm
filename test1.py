s = input()
ls = []
for c in s:
    ls.append(str(ord(c)))
print(",".join(ls))

s = input("请输入一个字符串：")
ls = []
for c in s:
    print(ord(c),end=',')



s = input()
for i in s:
    print(chr(ord(i)-3),end="")

s = input()
print(s[1:] + s[0])
n = input("请输入一个整数：")
print(pow(2, eval(n), pow(10, 10)))

n = input("请输入一个整数：")
print(len(str(eval(n)**2)))

height=input('how tall are you ,in inches?')
height=int(height)
if height >= 36:
    print('\nyou are tall enough to ride!')
else:
print('\nyou will be able to ride when you are a little older. ')

from turtle import *
color('red','pink')
begin_fill()
left(135)
fd(100)
right(180)
circle(50,-180)
left(90)
circle(50,-180)
right(180)
fd(100)
end_fill()
hideturtle()
done()

from turtle import *
setup(400,400)
penup()
goto(-100,50)
pendown()
color("red")
begin_fill()
for i in range(5):
    forward(200)
    right(144)
end_fill()
hideturtle()
done()

import turtle as t
t.colormode(255)
t.color(255,215,0)
t.begin_fill()
for x in range(8):
    t.forward(200)
    t.left(225)
t.end_fill()
t.hideturtle()
t.done()

import turtle as t
def tree(length,level):#树的层次
    if level <= 0:
        return
    t.forward(length)  #前进方向画 length距离
    t.left(45)
    tree(0.6*length,level-1)
    t.right(90)
    tree(0.6*length,level-1)
    t.left(45)
    t.backward(length)
    return
t.pensize(3)
t.color('green')
t.left(90)
tree(100,6)

N = int(input())
sum = 0
for i in range(1,N):
    if i % 2 == 1 :
        sum += i**2
print(sum)

N = eval(input())
s = 0
for i in range(1, N):
    if i % 2 == 1:
        s += i**2
print(s)


for i in range(100):
    if i % 2 == 0:
        print(i)

N = eval(input())
if N == 1:
    print('False')
for i in range(2,N):
    if N % i == 0:
        print('False')
else:
    print('True')



for i in range(2,101):
    result = True
    for m in range(2,i):
        if i % m == 0:
            result = False
    while result:
        print(i)



for i in range(2,101):
    result = True
    for m in range(2,i):
        if i % m == 0:
            result = False
        if result == True:
            print(i)


p = [2]
for i in range(2,101):
    for m in range(2,i):
        if i%m==0:
            break
        if m==i-1:
            p.append(i)
print(p)


def f(n):
    p=[2]
    for i in range(2,n+1):
        for m in range(2,i):
            if i%m==0:
                break
            if m==i-1:
                p.append(i)
    return p

result = True
for i in range(2,101):
    for m in range(2,i):
        if i%m==0:
            result=False
if result:
    print(i)

N = list(input())
M = []
for i in range(len(N)):
    M.append((int(N[i]))**2)
sum = 0
for m in range(len(M)):
    sum += M[m]
print(sum)


n = input()
sum = 0
for c in n:
    sum += (eval(c))**2
print(sum)

N = input()
sum = 0
while N != '':
    sum += eval(N)
    N = input()
print(sum)

while True:
    N = input()
    flag = True
    for i in N:
        if i in "0123456789":
            flag = False
            break
    if flag:
        break
print(N)


while True:
    try:
        N = input("请给出一个全数字输入: ")
        print(eval(N))
        break
    except:
        pass

while True:
    N = input()
    if type(eval(N)) == float:
        print(eval(N))
        break

while True:
    try:
        N = input()
        if type(eval(N)) == float:
            print(eval(N))
            # break
    except:
        pass

a,b = 1,2
ls = []
ls.append(str(a))
while b < 1000000:
    a,b = b, a**2+b**2
    ls.append(str(a))
print(",".join(ls))

a,b = 1,2
ls = []
ls.append(str(a))
while True:
    if b >= 1000000:
        break
    else:
        a,b = b,a**2+b**2
        ls.append(str(a))
print(",".join(ls))

import random
random.seed(17)
s = ""
for i in range(20):
    s += str(random.randint(0,999))
print(s)


import turtle
for i in range(4):
    turtle.right(90)
    turtle.circle(50,180)


ls = [23,41,32,12,56,76,35,67,89,44]
print(ls)
def bub_sort(s_list):
    for i in range(len(s_list)-1):
        is_change = True
        for j in range(len(s_list)-1-i):
            if s_list[j] > s_list[j+1]:
                s_list[j] , s_list[j+1] = s_list[j+1] , s_list[j]
                is_change = False
        if is_change:
            break
    return s_list
bub_sort(ls)
print(ls)


ls = [23,41,32,12,56,76,35,67,89,44]
print(ls)
def bub_sort(s_list):
    for i in range(len(s_list)-1):
        for j in range(len(s_list)-1-i):
            if s_list[j] > s_list[j+1]:
                s_list[j],s_list[j+1] = s_list[j+1],s_list[j]
    return s_list
bub_sort(ls)
print(ls)


ls = [23,41,32,12,56,76,35,67,89,44]
print(ls)
def bub_sort(s_list):
    for i in range(len(s_list)-1):
        is_change = True
        for j in range(len(s_list)-1-i):
            if s_list[j] > s_list[j+1]:
                s_list[j],s_list[j+1] = s_list[j+1],s_list[j]
                is_change = False
        if is_change:
            break
    return s_list
bub_sort(ls)


def longestCommonPrefix(self, strs):
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest


class Solution():
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

class Solution():
    def reverse(self, x):
        if x >= 2**31-1 or x <= -2**31: return 0
        else:
            strg = str(x)
            if x >= 0 :
                revst = strg[::-1]
            else:
                temp = strg[1:]
                temp2 = temp[::-1]
                revst = "-" + temp2
            if int(revst) >= 2**31-1 or int(revst) <= -2**31: return 0
            else: return int(revst)

class Solution:
    def isValid(self,s):
        d = {}
        for key in s:
            d[key] = d.get(key,0) + 1
        if d["("] == d[")"]:
            if d["["] == d["]"]:
                if d["{"] == d["}"]:
                    return "true"
        else:
            return "false"

class Solution:
    def isValid(self, s):
        while '{}' in s  or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''


x = ((3**4+5*6**7)/8)**0.5
print("{:.3f}".format(x))

import jieba
s = "中国特色社会主义进入新时代，我国社会主要矛盾已经转化为人民日益增长的美好生活需要和不平衡不充分的发展之间的矛盾。"
n = len(s)
m = len(jieba.lcut(s))
print("中文字符数为{}，中文词语数为{}。".format(n, m))

print("二进制{0:b}、十进制{0}、八进制{0:o}、十六进制{0:x}".format(0x4DC0+50))
print("二进制{0:b}、十进制{0}、八进制{0:o}、十六进制{0:X}".format(0x4DC0+50))

import turtle
d = 0
for i in range(4):
    turtle.fd(200)
    d = d + 90
    turtle.seth(d)

print(4, 200, 'd + 90')

ls = ["综合", "理工", "综合", "综合", "综合", "综合", "综合", "综合", "综合", "综合",\
      "师范", "理工", "综合", "理工", "综合", "综合", "综合", "综合", "综合","理工",\
      "理工", "理工", "理工", "师范", "综合", "农林", "理工", "综合", "理工", "理工", \
      "理工", "综合", "理工", "综合", "综合", "理工", "农林", "民族", "军事"]
d = {}
for key in ls:
    d[key] = d.get(key,0) + 1
for key in d.keys():
    print("{}:{}".format(key,d[key]),end="\n")

fr = open("论语-网络版.txt","r",encoding="utf-8")
fw = open("论语-提取版.txt","w",encoding="utf-8")
wflag = False            #写标记
for line in fr:
    if "【" in line:     #遇到【时，说明已经到了新的区域，写标记置否
        wflag = False
    if "【原文】" in line:  #遇到【原文】时，设置写标记为True
        wflag = True
        continue
    if wflag:    #根据写标记将当前行内容写入新的文件
        for i in range(40):
            for j in range(40):
                line = line.replace("{}·{}".format(i,j),"")
        line = line.replace(" ","")
        fw.write(line)
fr.close()
fw.close()

import re
fr = open("论语-提取版.txt","r",encoding="utf-8")
fw = open("论语-原文.txt","w",encoding="utf-8")
for line in fr:
    line = re.sub(r'（.*?）','',line)
    fw.write(line)
fr.close()
fw.close()

import turtle as t
def DrawCctCircle(n):
    t.penup()
    t.goto(0,-n)
    t.pendown()
    t.circle(n)
for i in range(20,80,20):
    DrawCctCircle(i)
t.done()

N = eval(input())   # N取值范围是0—100，整数
print("{:>3}%@{}".format(N,'='*(N//5)))

s = "学而时习之,不亦说乎?有朋自远方来,不亦乐乎?人不知而不愠,不亦君子乎?"
n = 0  # 汉字个数
m = 0  # 标点符号个数
m = s.count(',') + s.count('?')
n = len(s) - m
print("字符数为{}，标点符号数为{}。".format(n, m))

N = input()
s = 0
for i in range(eval(N),eval(N)+100):
    if i%2 == 1:
        s += i
print(s)

import turtle as t
for i in range(6):
    t.fd(5)
    t.left(60)

def getInput():
    while True:
        N = input()
        if type(eval(N)) == int:
            break
    return N
print(getInput())


def getInput():
    try:
        txt = input()   # "请输入整数: "
        while eval(txt) != int(txt):
            txt = input()   # "请输入整数: "
    except:
        return getInput()
    return eval(txt)
print(getInput())

fr = open("天龙八部-网络版.txt","r",encoding="utf-8")
fw = open("天龙八部-汉字统计.txt","w",encoding="utf-8")
txt = fr.read()
d = {}
for key in txt:
    d[key] = d.get(key,0) + 1
del d[" "]
del d["\n"]
m = []
for key in d.keys():
    m.append("{}:{}".format(key,d[key]))
fw.write(",".join(m))
fr.close()
fw.close()

import jieba
fr = open("天龙八部-网络版.txt","r",encoding="utf-8")
fw = open("天龙八部-词语统计.txt","w",encoding="utf-8")
txttxt = fr.read()
txt = jieba.lcut(txttxt)
d = {}
for key in txt:
    d[key] = d.get(key,0) + 1
del d[" "]
del d["\n"]
m = []
for key in d.keys():
    m.append("{}:{}".format(key,d[key]))
fw.write(",".join(m))
fr.close()
fw.close()

a,b = 0, 1
while a <= 100:
    print(a, end = ",")
    a,b = b,a+b

import time
timestr = "2020-10-10 10:10:10"
t = time.strptime(timestr, "%Y-%m-%d %H:%M:%S")
print(time.strftime("%Y年%m月%d日%H时%M分%S秒", t))

import turtle as t
for i in range(3):
    t.seth(i*120)
    t.fd(200)

d = {"数学":101, "语文":202, "英语":203, "物理":204, "生物":206}
d["化学"] = 205
d["数学"] = 201
del d["生物"]
for key in d.keys():
    print("{}:{}".format(d[key],key),end="\n")

import random
random.seed(0x1010)
keys = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
ls = []
excludes = ""
while len(ls) < 10:
    pwd = ""
    for i in range(10):
        pwd += keys[random.randint(0,len(keys)-1)]
    if pwd[0] in excludes:
        continue
    else:
        ls.append(pwd)
        excludes += pwd[0]
print('\n'.join(ls))