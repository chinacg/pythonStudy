# -*- coding:utf-8 -*-

"""

@author:chinacg

@file:使用元类.py

@time:2017-12-1115:13

"""


# type()函数既可以返回一个对象的类型，又可以创建出新的类型，
# 比如，我们可以通过type()函数创建出Hello类，
# 而无需通过class Hello(object)...的定义：


def fn(self, name='world'):
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class

h = Hello()
h.hello()

# metaclass

'''除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。

metaclass，直译为元类，简单的解释就是：

当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。

但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。

连接起来就是：先定义metaclass，就可以创建类，最后创建实例。

所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。

metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用metaclass的情况，
所以，以下内容看不懂也没关系，因为基本上你不会用到。

我们先看一个简单的例子，这个metaclass可以给我们自定义的MyList增加一个add方法：

定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：'''


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：

class MyList(list, metaclass=ListMetaclass):
    pass


'''__new__()方法接收到的参数依次是：

当前准备创建的类的对象；

类的名字；

类继承的父类集合；

类的方法集合。

测试一下MyList是否可以调用add()方法：'''

L = MyList()
L.add(1)
print(L)

'''动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？正常情况下，确实应该直接写，通过metaclass修改纯属变态。

但是，总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。

ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。

要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

让我们来尝试编写一个ORM框架。'''


# 首先来定义Field类，它负责保存数据库表的字段名和字段类型：

class Field(object):
    __slots__ = ('__name', '__colunm_type')

    def __init__(self, name, colunm_type):
        self.__name = name
        self.__colunm_type = colunm_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.__name)

    def __getattr__(self, item):
        if item == '__name'[2:]:
            return self.__name
        if item == '__colunm_type'[2:]:
            return self.__colunm_type
        raise AttributeError('%s has no attribute %s' % (self.__class__.__name__, item))


# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：

class StringField(Field):
    __slots__ = Field.__slots__

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    __slots__ = Field.__slots__

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute %s" % item)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()

#  这里没有返回User类中的IntegerField 类型， 因为我们在元类中已经对其进行了集中处理，

#  在元类的__new__方法中我们对即将要生成的类进行了拦截和属性替换，原本用户定义的一系列Field对象被映射到了值上面

#  而原本的类属性被删除。更深一步， 我们甚至可以定义一个api 根据key返回从数据库中取得的数据 u= User(id=12345)
print(u['id'])




