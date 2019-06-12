# -*- coding: utf-8 -*-


class Test(object):

    def __init__(self):
        print("&&&&&&&& ", type(self))
        print("******** ", self.__class__)

    @staticmethod
    def static_method(*args):

        return "This is static method. argss: {}".format(args)

    @classmethod
    def cls_method(cls, *args):

        return "This is cls method."

    def instance_method(self):

        return "This is instance method."


if __name__ == '__main__':

    a = Test.static_method(1, 2, 3)
    print(a)

    b = Test().cls_method()
    c = Test.cls_method()

    print(b)
    print(c)

    print(Test().instance_method())
