# -*- coding:utf-8 -*-

"""

@author:chinacg

@file:use@property.py

@time:2017-12-0815:32

"""


# Python内置的@property装饰器就是负责把一个方法变成属性调用的：

class Product(object):
    __slots__ = ('__name')

    def __init__(self, name=''):
        self.__name = name

    @property
    def name(self):
        return self.get_name()

    @name.setter
    def name(self, name):
        self.set_name(name)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


p1 = Product(name='p1')

print(p1.get_name())

p1.set_name('p2')

print(p1.get_name())

print(p1.name)

p1.name = 'p3'

print(p1.name)


# 练习 请利用@property给一个Screen对象加上width和height属性，
# 以及一个只读属性resolution：

class Screen(object):
    __slots__ = ('__width', '__height', '__resolution')

    def __init__(self, width=0, height=0, resolution=0):
        self.__width = width
        self.__height = height
        self.__resolution = resolution

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def resolution(self):
        self.__resolution = self.height * self.width
        return self.__resolution


s = Screen()
s.width = 1024
s.height = 768
print('resolution', s.resolution)