# -*- coding: utf-8 -*-

from types import MappingProxyType


class DictUnchange(object):
    """
    字典 不可变
    """

    def __init__(self):
        self.item = dict()

    def __call__(self, key, value):
        self.item[key] = value
        return MappingProxyType(self.item)


def dict_unchange(key, value):
    item = dict()
    item[key] = value
    try:
        result = MappingProxyType(item)
    except TypeError as err:
        raise err

    return result


item = dict()


def dict_key_set_one(key, value):

    if key in item:
        print("此 key 已被设置过，请设置新的key值")
    item[key] = value

    return MappingProxyType(item)


if __name__ == '__main__':

    d = DictUnchange()
    dd = d('animal', 'giraffe')
    print(dd, type(dd))

    try:
        dd['animal'] = 'cat'
    except TypeError as e:
        print(e)

    d_1 = dict_unchange('fruit', 'apple')
    print(d_1, type(d_1))

    print(d_1['fruit'])

    try:
        d_1['fruit'] = 'orange'
    except TypeError as e:
        print("d_1 字典不能更改")

    ddd = dict_key_set_one('code', 'python')
    dict_key_set_one('code', 'c')
    print(ddd, type(ddd))
