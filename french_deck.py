# -*- coding: utf-8 -*-

from collections import namedtuple
from random import shuffle


class FrenchDeck:

    Card = namedtuple('Card', ['rank', 'suit'])
    # print(Card('aa', 13))
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
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


def set_card(deck, pos, card):

    deck._cards[pos] = card


if __name__ == '__main__':

    deck = FrenchDeck()
    print(deck._cards)

    # 猴子补丁
    FrenchDeck.__setitem__ = set_card

    # 打乱原来的列表的顺序
    shuffle(deck)
    print(deck[:5])

    print(deck[0])
    print(deck[0].rank, deck[0].suit)
    print(dir(deck[0]))
    print(len(deck))






