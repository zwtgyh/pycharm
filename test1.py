import re
re.escape("www.python.org")
re.escape("But where is the ambiguity")

a = input("Please enter your name: ")
print("Hello, " + a + " !")


x = int(input("Please enter a random number: "))
if x == 66:
    print("你真是个帅B")
else:
    print("你真是个宋希文")

print('Let\'s go!')
print("Let's go")

DaysPeryear = int(input("Please enter days: "))
HoursPerday = int(input("please enter hours: "))
MinutesPerhour = int(input("Please enter minutes: "))
SecondsPerminute = int(input("Please enter seconds: "))
result = DaysPeryear * HoursPerday * MinutesPerhour * SecondsPerminute
print(result)

s = '1234fdfdfd'
s.isalnum()

year = int(input("Please enter a year: "))
x = year % 400
y = year % 4
z = year % 100
if x == 0:
    print('bingo!')
else:
    if y == 0 and z != 0:
        print('bingo')
    else:
        print('no')

x = int(input("Please enter a number: "))
if x%2 == 0:
#if x/2 == int(x/2):
    print("偶数")
else:
    print("奇数")

not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9

for i in range(101):
   #if i%2 == 0:
    if i%2 != 0:
        print(i)
for n in range(999):
    if n % 2 == 1 and n % 3 == 2 and n % 5 == 4 and n % 6 == 5 and n % 7 == 0:
        print(n)

