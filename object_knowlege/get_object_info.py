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
    name = 'PreStudent'  # 类属性

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

print(Lily.name)


# 练习 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：

class AfterStudent(Student):
    count = 0

    def __init__(self, name, score, gender):
        super().__init__(name, score, gender)
        AfterStudent.count += 1  # 类属性操作


# 测试:
if AfterStudent.count != 0:
    print('测试失败!')
else:
    bart = AfterStudent('Bart', 30, 1)
    if bart.count != 1:
        print('测试失败!')
    else:
        lisa = AfterStudent('Bart', 60, 1)
        if lisa.count != 2:
            print('测试失败!')
        else:
            print('Students:', AfterStudent.count)
            print('测试通过!')


# 还可以尝试给实例绑定一个方法：

def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


mila = AfterStudent('mila', 90, 2)

mila.set_age = types.MethodType(set_age, mila)  # 给实例绑定一个方法

mila.set_age(24)

print(mila.age)

# 为了给所有实例都绑定方法，可以给class绑定方法：

AfterStudent.set_age = set_age

qila = AfterStudent('qila', 89, 2)

qila.set_age(34)

print(qila.age)


# 为了达到限制的目的，Python允许在定义class的时候，
# 定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

class SlotStudent(Student):
    __slots__ = ('height', 'age', '__name', '__score', '__gender')  # 用tuple定义允许绑定的属性名称

    def __init__(self, name, score, gender):
        self.__name = name
        self.__score = score
        self.__gender = gender


sily = SlotStudent('sily', 45, 2)
sily.height = 1.55
sily.age = 34

print('sily\'s height is %.2f and age is %d' % (sily.height, sily.age))

sily.color = 'yellow'

print(sily.color)
