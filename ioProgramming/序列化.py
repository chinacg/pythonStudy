# -*- coding:utf-8 -*-

"""

@author:chinacg

@file:序列化.py

@time:2017-12-1916:51

"""
import json
import pickle

with open('dump.txt', 'wb') as f:
    pickle.dump(dict(name='bob', age='21', score='90'), f)

with open('dump.txt', 'rb') as f:
    print(pickle.load(f))

# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。
# 我们先看看如何把Python对象变成一个JSON：

d = dict(name='Bob', age=20, score=88)
j = json.dumps(d)
print(j)

# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，
# 后者从file-like Object中读取字符串并反序列化：

d = json.loads(j)

print(d, type(d))


# JSON进阶

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))


# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。

# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


print(json.loads(json.dumps(s, default=lambda obj: obj.__dict__), object_hook=dict2student))
