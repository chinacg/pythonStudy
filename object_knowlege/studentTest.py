# -*- coding:utf-8 -*-

"""

@author:chinacg

@file:studentTest.py

@time:2017-12-0715:13

"""
from object_knowlege.student import Student

bart = Student('Bart Simpson', 78, 1)

lisa = Student('Lisa Simpson', 89, 2)

bart.print_score()

lisa.print_score()

print(bart.get_grade())

print(lisa.get_grade())


