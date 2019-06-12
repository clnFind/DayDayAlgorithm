# -*- cofing: utf-8 -*-


class AttrDict(dict):

    def __getattr__(self, key):

        if key not in self:
            raise AttributeError

        return self[key]

    def __setattr__(self, key, value):

        if key not in self:
            raise AttributeError

        self[key] = value


def get_params():

    aa = {}
    a = 2
    b = 1

    # locals() 返回一个从作用域中所有局部变量名到值的映射
    print(locals())

    return AttrDict(locals())


if __name__ == '__main__':

    d = AttrDict(a=1, b=2, c=3)
    print(d, d.a, d.c)

    r = get_params()
    print(r, type(r))

    # 利用属性访问字典
    print(r.a, r['a'])
    r['a'] = 222
    print(r)

    ret = AttrDict()
    # ret['size'] = 99
    ret['size'] = 100
    print(ret, ret.size)
    print(dir(ret))
