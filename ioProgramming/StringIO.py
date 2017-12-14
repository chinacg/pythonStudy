# -*- coding:utf-8 -*-

"""

@author:chinacg

@file:StringIO.py

@time:2017-12-1413:46

"""
from datetime import datetime
from io import StringIO, BytesIO

import os

'''很多时候，数据读写不一定是文件，也可以在内存中读写。

StringIO顾名思义就是在内存中读写str。

要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：'''

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')

print(f.getvalue())

# getvalue()方法用于获得写入后的str。

# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：

f = StringIO('Hello!\nHi!\nGoodbye')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

'''BytesIO

StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：'''

f = BytesIO()
f.write('中文'.encode('utf-8'))

print(f.getvalue())

'''请注意，写入的不是str，而是经过UTF-8编码的bytes。

和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：'''

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')

print(f.read())

# 操作文件和目录
# 查看当前目录的绝对路径:
absPath = os.path.abspath('.')
print(absPath)

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
# 这样可以正确处理不同操作系统的路径分隔符
new_path = os.path.join(absPath, 'testdir')
if not os.path.exists(new_path):
    os.mkdir(new_path)
    print('%s is made.' % new_path)
else:
    print('%s is already exit, will delete it... ' % new_path)
    os.rmdir(new_path)
    print('deleted.')

# 同样的道理，要拆分路径时，也不要直接去拆字符串，
# 而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

new_path = os.path.join(new_path, 'test.txt')
pathT = (os.path.split(new_path), os.path.splitext(new_path)[1])

# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：


print('folder is %s and file name is %s suffix is %s .' % (pathT[0][0], pathT[0][1], pathT[1]))

# 对文件重命名：

test_path = os.path.join(os.path.abspath('.'), 'test.py')
if os.path.exists(test_path):
    print('test.py is exit, rename it...')
    a = os.path.join(os.path.abspath('.'), 'a.py')
    if os.path.exists(a):
        os.remove(a)
    os.rename(test_path, 'a.py')
    print('rename over.')
else:
    with open(test_path, 'w') as f:
        print('test.py is not exit, create test.py directly...')
        f.write('print ( "hello,world" )')
        print('created over.')

# 练习

# 1.利用os模块编写一个能实现dir -l输出的程序。

pwd = os.path.abspath('.')

print('          size    Last Modified Name ')
print('-' * 40)

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))


# 2.编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

def find_file(name):
    pwd = os.path.abspath('.')

    def f__(path):
        for f in os.listdir(path):
            if os.path.isfile(f) and f.find(name) != -1:
                print(os.path.join(path, f))
            elif os.path.isdir(f):
                f__(f)

    f__(pwd)


find_file('y')
