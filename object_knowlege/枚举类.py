# -*- coding:utf-8 -*-

"""

@author:chinacg

@file:枚举类.py

@time:2017-12-1114:56

"""

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：

from enum import Enum, unique


@unique
class WeekDay(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(WeekDay.Sun, WeekDay['Sun'], WeekDay.Thu.value)


# 练习 把Student的gender属性改造为枚举类型，可以避免使用字符串：

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


@unique
class Gender(Enum):
    Male = 0
    Female = 1
