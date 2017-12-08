# -*- coding:utf-8 -*-

"""

@author:chinacg

@file:get_object_info.py

@time:2017-12-089:59

"""

#  使用type() 判断对象类型
import types

from object_knowlege.student import Student

print(type(1123))

print(type(abs))


def fn():
    pass


exec('print(type(fn))')

print(type(fn) == types.FunctionType)

print(type(lambda x: x) == types.LambdaType)


# 使用 isinstance() 对于class的继承关系来说，
# 使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。



class PreStudent(Student):
    def __init__(self, name, score, gender, pre_order=0):
        super().__init__(name, score, gender)
        self.pre_order = pre_order  # 自定义的非私有变量，外界可以直接通过实例访问

    def __len__(self):
        return 10

    def run(self):
        print('running')


Lily = PreStudent('Lily', 90, 1)

print(isinstance(Lily, PreStudent) and isinstance(Lily, Student))

# 使用dir() 获得一个对象的所有属性和方法，
# 可以使用dir()函数，它返回一个包含字符串的list，
# 比如，获得一个str对象的所有属性和方法：

print('__len__' in dir(Lily))

print(len(Lily))

# hasattr 测试对象是否包含某个属性：

if hasattr(Lily, 'pre_order'):
    print(Lily.pre_order)

# 设置属性
setattr(Lily, 'test', 'test')

print(Lily.test)

# 获取属性

print(getattr(Lily, 'test'))

# 可以传入一个default参数，如果属性不存在，就返回默认值：

print(getattr(Lily, 'z', list(x * x for x in range(0, 10))))

# 可以获取对象的方法

run = getattr(Lily, 'run')

run()