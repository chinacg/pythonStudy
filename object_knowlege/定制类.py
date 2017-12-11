# -*- coding:utf-8 -*-

"""

@author:chinacg

@file:定制类.py

@time:2017-12-1113:40

"""


class Student(object):
    """Student class for example"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        # __str__  只需要定义好__str__()方法，返回一个好看的字符串就可以了
        return 'Student object (name: %s)' % self.name

    def __getattr__(self, attr):
        # __getattr__ 方法，动态返回一个属性
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 88  # 可以返回方法
        raise AttributeError('\'Student\' object has no attribute: %s' % attr)

    __repr__ = __str__


print(Student('bibi'))
print(Student.__doc__)
s = Student('lili')
print(s.age(), s.score)  # 动态属性方法需要修改调用方式 s.age()


# 利用完全动态的__getattr__，我们可以写出一个链式调用：

class Chain(object):

    def __init__(self, path=''):
        self.__path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.__path, path))

    def __call__(self, *args):
        for arg in args:
            return Chain(self.__path + ':%s' % arg)

    def __str__(self):
        return self.__path


print(Chain().status.users('user').timeline.list.makes('make1'))
