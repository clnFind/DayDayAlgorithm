# -*- coding: utf-8 -*-


def record_factory(cls_name, field_names):
    """
    类工厂函数，实现类似于 collections.namedtuple 的命名元组
    :param cls_name:
    :param field_names:
    :return:
    """

    try:
        field_names = field_names.replace(',', ' ').split()
    except AttributeError:
        pass
    field_names = tuple(field_names)

    print("cls_name:  ", cls_name, "fff: ", field_names)

    def __init__(self, *args, **kwargs):

        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)

    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):
        values = ', '.join("{}={!r}".format(*i) for i in zip(self.__slots__, self))

        return "{}({})".format(self.__class__.__name__, values)

    cls_attrs = dict(__slots__=field_names,
                     __init__=__init__,
                     __iter__=__iter__,
                     __repr__=__repr__
                     )

    print("cls_attrs:  ", cls_attrs)
    # type是一个类，传入三个参数，构建一个新类 （类，基类，dict）
    return type(cls_name, (object,), cls_attrs)


if __name__ == '__main__':
    Dog = record_factory('Dog', 'name age')
    print("Dog.......: ", Dog)
    print("^^^^^^^^^^^^")
    n = Dog('jam', 2)
    print(n, '\n', n.name)
