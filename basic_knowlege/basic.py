import math

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(classmates[-1])
classmates.append('Adam')
print(classmates)

classmatesT = ('Michael', 'Bob', 'Tracy')
print(classmatesT)

# 定义空tuple
t = ()
print('空tuple:', t)
# 定义只有一个元素的tuple
t = (1,)
print('一个元素的元组：', t)

# 练习 请用索引取出下面list的指定元素：

# -*- coding: utf-8 -*-

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

height = 1.75
weight = 80.5

bmi = weight / (height * height)
# bmi = 20
if bmi < 18.5:
    print("too light")
elif 18.5 < bmi < 25:
    print("normal")
elif 25 < bmi < 28:
    print("little heavy")
elif 28 < bmi < 32:
    print("fat")
elif bmi > 32:
    print("even fat")

for name in classmates:
    print(name)

# loop sum using 'for'
sum_numbers = 0
for n in range(101):
    sum_numbers += n
print(sum_numbers)

# loop sum using 'while'

sum_numbers = 0
n = 99
while n > 0:
    sum_numbers += n
    n -= 2
print(sum_numbers)

# 练习 请利用循环依次对list中的每个名字打印出Hello, xxx!：

L = ['Bart', 'Lisa', 'Adam']

# using for loop

for name in L:
    print("Hello,", name)

# using while loop

n = len(L)
while n > 0:
    print("Hello", L[0 - n])
    n -= 1

# break

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n += 1
print('END')

# continue

n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)

# dict
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print('Michael\'s score is ', d['Michael'])
print('Green' in d)
print(d.get('Micheal', -1))
print(d.pop('Bob'))
print('Bob is in dict? ', 'Bob' in d)

# set

s = set([1, 2, 3, 3])
print(s)
s.add(4)
print(s)
s.remove(1)
print(s)

s_1 = {2, 3, 5}
print(s & s_1)
print(s | s_1)

# Function

print(abs(-20))

n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))

from basic_knowlege.abs_teset import my_abs

print(my_abs(-190))


# blank function

def nop():
    pass


print(nop())


# print(my_abs("W"))  # throw exception type


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)


# default parameter

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
    pass


print(enroll('Bob', 'M'))


# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


print(calc(1, 2, 3))


# 关键字参数

def person(name, age, **kwargs):
    print('name:', name, ' age:', age, ' other:', kwargs)


person('Bob', 34, city='Beijing')
person('Adam', 46, gender='M', job='Engineer')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


# 命名关键字参数
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person_v2(name, age, *, city, job):
    print(name, age, city, job)



person('Jack', 33, city='Beijing', job='Enginner')


def person_v3(name, age, *kwargs, city='Beijing', job):
    print(name, age, kwargs, city, job)


person_v3('Jack', 44, job="Enginner")
person_v3('Job', 45, 1, 2, 3, job='Enginner')


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1('a', 'b', 1, 2, 4, position='Beijing')
f2('a', 'b', d='d', height=17)


# 练习 可接收一个或多个数并计算乘积：

def product(*kwargs):
    sum = 1
    for n in kwargs:
        if not isinstance(n, (int, float)):
            raise TypeError('type error', n)
        sum *= n
    return sum


print(product(*(1, 2, 3, 6, 5)))


# 递归函数 汉诺塔

def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(3, 'A', 'B', 'C')

# 切片

L = ["Michael", "Sarch", 'Tracy', 'Bob', 'Jack']

print(L[:])
print(L[:4])
print(L[:-1])
print(L[0:1])
print(list(range(100))[:10])


# 练习 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：

def trim(s):
    ss = s
    if not isinstance(s, str):
        raise TypeError('type is not string')
    if len(s) <= 0:
        raise IndexError('blank string')

    i, j, size = 0, len(s) - 1, len(s)
    while ss[i] == ' ' and i < size - 1:
        i += 1
    while ss[j] == ' ' and j > 1:
        j -= 1

    print(ss[i:j + 1])


    # while ss[0] == ' ' and len(ss) > 1:
    #     ss = ss[1:]
    # while ss[-1] == ' ' and len(ss) > 1:
    #     ss = ss[:-1]
    # print('^'+ss + '$')


trim("   ")

# 迭代

for key, value in d.items():
    print('key:', key, 'value:', value)

from collections import Iterable

print(isinstance('abc', Iterable))  # 判断是否可以做迭代
print(isinstance([1, 2, 3], Iterable))
print(isinstance(1, Iterable))

for k, v in enumerate(['A', 'B', 'C']): # 数组转迭代器 key是index
    print('key:', k, 'value:', v)


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

def findMinAndMax(L):
    if not isinstance(L, list):
        raise TypeError('input is not list')
    if len(L) == 0:
        raise IndexError('len is 0')
    for k, v in enumerate(L):
        if k < len(L) - 1:
            if v > L[k + 1]:
                temp = L[k + 1]
                L[k + 1] = L[k]
                L[k] = temp
    return L[0], L[-1]


print(findMinAndMax([1, 3, 4, 0, 2]))

# 列表生成式

L = list(range(0, 10))

print(L)

L = []
for x in range(1, 11):
    L.append(x * x)

print(L)

print(list(x * x for x in range(1, 11)))
print([x + y for x in "AVB" for y in "rts"])

# 练习 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：

L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = list(x.lower() for x in L1 if isinstance(x, str))

print(L2)

# 生成器

g = (x * x for x in range(10))
for n in g:
    print(n)


# 练习 输出杨辉三角

def triangles():
    result_L = [1]
    while True:
        yield result_L
        R = [1]
        for i, v in enumerate(result_L):
            if 0 < i <= len(result_L) - 1:
                R.append(result_L[i - 1] + result_L[i])
        R.append(1)
        result_L = R
    return "done"


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break




