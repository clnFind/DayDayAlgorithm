# -*- coding:utf-8 -*-

import time
import functools


def singleton(cls):
    """
    类装饰器
    单例模式
    """
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance


@singleton
class MyClass(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


def clock(func):
    """
    函数装饰器
    :param func:
    :return:
    """

    # 闭包函数
    def clocked(*args):

        t1 = time.perf_counter()
        result = func(*args)
        t = time.perf_counter() - t1
        name = func.__name__

        str_arg = ', '.join(repr(s) for s in args)
        print("[%0.8fs] %s(%s) --> %r " % (t, name, str_arg, result))
        # rst.append(str_arg)

        return result
    return clocked


def clock_1(func):

    @functools.wraps(func)              # 获取被装饰函数的属性（函数名、参数）
    def clocked(*args, **kwargs):
        t1 = time.perf_counter()
        result = func(*args, **kwargs)
        t = time.perf_counter() - t1
        name = func.__name__

        print("[%0.8fs] %s(%s) --> %r " % (t, name, args, result))

        return result
    return clocked


@clock
def snooze(seconds):

    time.sleep(seconds)


@clock_1
def factorial(n):

    return n if n < 2 else n*factorial(n-1)


# 使用后速度更快  least recently used cache; 装饰的参数要求是可散列的
# 默认参数值 maxsize=128, typed=False
@functools.lru_cache()          # 函数缓存
@clock
def fibonacci(n):

    if n < 2:
        return n

    return fibonacci(n-2) + fibonacci(n-1)


if __name__ == '__main__':
    print('\n')
    print("--" * 20, "Calling snooze(.123)")
    snooze(.123)

    print("--" * 20, "Calling factorial(6)")

    print("6! = ", factorial(6))

    print(factorial.__name__)

    print(fibonacci(10))
