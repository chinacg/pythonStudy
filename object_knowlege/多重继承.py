# -*- coding:utf-8 -*-

"""

@author:chinacg

@file:多重继承.py

@time:2017-12-0816:58

"""


class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物:
class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


class Runnable(object):
    def run(self):
        print('Running...')


class RunnableEx(object):
    def run(self):
        print('Running ex...')


class Flyable(object):
    def fly(self):
        print('Flying...')


class Dog(Mammal, RunnableEx, Runnable ):
    pass


class Bat(Mammal, Flyable):
    pass


dog = Dog()

dog.run()
