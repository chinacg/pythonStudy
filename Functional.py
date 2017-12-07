# 传入函数
import datetime
from functools import reduce
from types import FunctionType

from collections import Iterable

import functools


def add(x, y, func):
    if not isinstance(func, FunctionType) and not hasattr(func, '__call__') and not callable(func):
        raise TypeError('func is not callable type')
    else:
        return func(x) + func(y)


print(abs)
print(add(-5, 6, abs))

# map/reduce

# 把str转换为int的函数

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int('123456'))

print(isinstance([1], Iterable))


# 练习 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
# 其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def normalize(name):
    if not isinstance(name, Iterable):
        raise TypeError(' name is not Iterable type ')
    else:
        return list(map(lambda x: str(x).lower().capitalize(), name))
    pass


L1 = ['adam', 'LISA', 'barT']

print(normalize(L1))


# 练习 Python提供的sum()函数可以接受一个list并求和，
# 请编写一个prod()函数，可以接受一个list并利用reduce()求积：

def prod(L):
    if not isinstance(L, list):
        raise TypeError(' L is not type list ')
    else:
        return reduce(lambda x, y: x * y, L)
    pass


print(prod([3, 5, 7, 9]))


# 练习 利用map和reduce编写一个str2float函数，
# 把字符串'123.456'转换成浮点数123.456：


def str2float(s):
    if not isinstance(s, str):
        raise TypeError(' s is not str ')
    else:
        l = list(map(lambda x: DIGITS[x], s.replace('.', '')))
        p = s.find('.')
        p = 0 if p == -1 else len(s) - p - 1
        if p != 0:
            return reduce(lambda x, y: x * 10 + y, l) / 10 ** p
        else:
            return reduce(lambda x, y: x * 10 + y, l)
        pass


print(str2float('12334.034'))


# filter

# 练习 回数是指从左向右读和从右向左读都是一样的数，
# 例如12321，909。请利用filter()筛选出回数：


def is_plindrome(n):
    if not isinstance(n, int):
        raise TypeError(n, ' is not int type ')
    else:
        l, l_r = [], []
        i = 0
        for s in str(n):
            l.append(s)
            l_r.insert(i, s)
            ++i
    return l == l_r


print(list(filter(is_plindrome, range(1, 1000))))

# sorted

# 练习 假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# 请用sorted()对上述列表分别按名字排序：

def by_name(t):
    if not isinstance(t, Iterable):
        raise TypeError(' t is not Iterable type')
    return sorted(t, key=lambda x: str(tuple(x)[0]).lower())


print(by_name(L))


# 再按成绩从高到低排序：

def by_score(t):
    if not isinstance(t, Iterable):
        raise TypeError(' t is not Iterable type')
    return sorted(t, key=lambda x: tuple(x)[1], reverse=True)


print(by_score(L))


# 返回函数
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
# 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。


# 练习 利用闭包返回一个计数器函数，每次调用它返回递增整数：

def createCounter():
    t = 0

    def counter():
        nonlocal t
        t += 1
        return t

    return counter


counterA = createCounter()
print(counterA(), counterA())

# 匿名函数

L = list(filter(lambda x: x % 2 == 1, range(1, 20)))

print(L)


# 装饰器
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("call %s():" % func.__name__)
        return func(*args, **kwargs)

    return wrapper


@log
def now():
    print("2017-12-06")


f = now
f()

print(f.__name__)


# 练习 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        time_start =
        r = fn(*args, **kwargs)
        print('{} executed in {} ms'.format(fn.__name__, (time.microsecond - time_start) * 1000))
        return r

    return wrapper


@metric
def show():
    print("hello, world!")


show()
