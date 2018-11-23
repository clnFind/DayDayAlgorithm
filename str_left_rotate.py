# -*- coding: utf-8 -*-
import time

"""
使用两种方法实现 字符串左移 n 位
第一种借鉴网络上的代码
第二种自己实现的
"""


class Solution:

    def __init__(self, strs, n):
        self.strs = strs
        self.n = n

    def left_rotate_string(self):
        if len(self.strs) < self.n or self.n < 1:
            return self.strs
        str_list = list(self.strs)
        self.reverses(str_list)
        length = len(self.strs)
        index = length - self.n
        front_list = self.reverses(str_list[:index])
        print(front_list)
        behind_list = self.reverses(str_list[index:])
        print(behind_list)
        result = ''.join(front_list) + ''.join(behind_list)
        return result

    def reverses(self, alist):

        if alist == None or len(alist) <= 0:
            return ''
        start_index = 0
        end_index = len(alist) - 1
        while start_index < end_index:
            alist[start_index], alist[end_index] = alist[end_index], alist[start_index]
            start_index += 1
            end_index -= 1
        return alist


def reverse_str(strs, n):
    """
    使用内置方法实现reverse
    内置方法 效率更高
    :param strs:
    :param n:
    :return:
    """

    if len(strs) < n or n < 1:
        return strs

    s_reverse = list(strs)
    s_reverse.reverse()

    index = len(strs) - n
    front = s_reverse[:index]
    front.reverse()

    back = s_reverse[index:]
    back.reverse()

    return ''.join(front) + ''.join(back)


if __name__ == '__main__':

    test = '123456'
    t1 = time.time()
    s = Solution(test, 2)
    print(s.left_rotate_string())
    t2 = time.time()
    print("使用循环迭代耗时： ", t2-t1)

    t3 = time.time()
    l = reverse_str(test, 2)
    print(l)
    t4 = time.time()
    print("使用内置reverse耗时： ", t4-t3)
    if t4-t3 < t2-t1:
        print(True)

