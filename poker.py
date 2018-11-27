# -*- coding: utf-8 -*-

from collections import namedtuple
from random import shuffle


class Poker:

    Card = namedtuple('Card', ['rank', 'suit'])
    # print(Card('aa', 13))
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')

    # 黑桃spades 方块diamonds 梅花clubs 红桃hearts
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [self.Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):

        return len(self._cards)

    def __getitem__(self, pos):

        return self._cards[pos]

    # def __setitem__(self, pos, val):
    #     rst = self._cards[pos] = val
    #
    #     return rst


def set_card(poker, pos, card):

    poker._cards[pos] = card


if __name__ == '__main__':

    poker = Poker()
    print(poker._cards)

    # 猴子补丁
    Poker.__setitem__ = set_card

    # 打乱扑克牌的顺序
    shuffle(poker)
    print(poker[:5])

    print(poker[0])
    print(poker[0].rank, poker[0].suit)
    print(dir(poker[0]))
    print(len(poker))







