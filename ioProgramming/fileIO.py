# -*- coding:utf-8 -*-

"""

@author:chinacg

@file:fileIO.py

@time:2017-12-1413:31

"""

try:
    f = open('./test.txt', 'r')
    for line in f.readlines():
        print(line.strip())
except IOError as e:
    print(e)
finally:
    f.close()

#  要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：

f = open('./a.jpg', 'rb')
f.read()

#  要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：

f = open('/test.txt', 'r', encoding='gbk')

# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，
# open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：

f = open('./test.txt', 'r', encoding='gbk', errors='ignore')

# 写文件

# 写文件和读文件是一样的，
# 唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
f = open('./test.txt', 'w')
f.write('Hello, world!')
f.close()

# 你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，
# 而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，
# 操作系统才保证把没有写入的数据全部写入磁盘。
# 忘记调用close()的后果是数据可能只写了一部分到磁盘，
# 剩下的丢失了。所以，还是用with语句来得保险：

with open('./text.txt', 'w') as f:
    f.write('Hello, world!')





