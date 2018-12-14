# -*- coding: utf-8 -*-


def find_first_unique_char(s):
    """
    字符串中找到第一个出现的唯一字符
    :param s:
    :return:
    """

    char_dict = dict()
    unique_char = list()

    for char in s:
        if char_dict.get(char):
            unique_char.remove(char)
        else:
            print(unique_char)
            unique_char.append(char)

        char_dict[char] = True

    print(unique_char)
    return unique_char[0]


if __name__ == '__main__':

    s = "asdfgashdgflpooh"

    r = find_first_unique_char(s)

    print(r)

