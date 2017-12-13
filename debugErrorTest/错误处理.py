# -*- coding:utf-8 -*-

"""

@author:chinacg

@file:错误处理.py

@time:2017-12-1311:02

"""

# try

try:
    print('try ...')
    r = 10 // int('a')
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
    raise
except ValueError as e:
    print('ValueError:', e)
    raise
else:
    print('no error!')
finally:
    print('finally...')
print('END')
