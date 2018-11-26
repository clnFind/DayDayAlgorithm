# -*- coding:utf-8 -*-


"""
单例模式的两种实现：元类 和 类装饰器
"""


class Singleton(type):
    """
    单例模式
    """
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class ClassTest(metaclass=Singleton):
    a = 1
    b = 2


class ClassTestNo(object):
    a = 1
    b = 2


def singleton(cls, *args, **kwargs):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance


def singleton1(cls):
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance


@singleton1
class MyClass(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


if __name__ == '__main__':

    # 装饰起模式
    m = MyClass()
    print(m.x)
    m1 = MyClass()
    m2 = MyClass()
    print(id(m1), id(m2))

    # 不带装饰起的类测试
    first = ClassTestNo()
    second = ClassTestNo()
    # id 不同，创建了两个实例
    print(id(first), id(second))

    # 元类为单例模式
    one = ClassTest()
    print(one.a)
    two = ClassTest()
    print(two.b)
    two.c = 3
    print(one.c)
    # id相同，只有一个实例
    print(id(one), id(two))


