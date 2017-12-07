# -*- coding:utf-8 -*-

"""

@author:chinacg

@file:student.py

@time:2017-12-0715:10

"""


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
