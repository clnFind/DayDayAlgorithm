# -*- coding: utf-8 -*-

from collections import abc
import keyword


class FrozenJSON:
    """
    以动态属性 访问 json 数据
    例如 d = {'name': 'xxx', 'identify': 'xxx'},
        f = Class(d)
        f.name = 'xxx'
    """

    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            print("Test hasattr......")
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


class FrozenJSON1:

    def __new__(cls, arg):
        print("classss: ", cls, arg)
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            print("argssss : ", arg)
            return arg

    def __init__(self, mapping):
        self.__data = dict(mapping)

        # 判断键值是否为关键词，经测试没效果
        # for key, value in mapping.items():
        #     if keyword.iskeyword(key):
        #         key += '_'
        #         print("^^^^^^^^: ", key)
        #     self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            print("######: ", self.__data)
            return FrozenJSON1(self.__data[name])


if __name__ == '__main__':

    f = FrozenJSON({'name': 'jack'})
    print(f, type(f))
    print(f.name)
    print(f.items(), f.keys(), '\n')

    ff = FrozenJSON1({'name': 'Tom', 'async': 2})

    print(ff.name)
    print(getattr(ff, 'async'))
