#!/usr/bin/env python3
import random
from collections import deque

class Card:

    suits = {
        'spade' : '\u2660',
        'heart' : '\u2665',
        'diamond' : '\u2666',
        'club' : '\u2663',
    }

    def __init__(self,rank,suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
       return '{}{}'.format(self.rank,self.suit)

    def __repr__(self):
        return self.__str__()

class Deck:
    
    def __init__(self,shuffle=True):
        self.cards = deque()
        for suit in ('spade','heart','diamond','club'):
            for rank in [2,3,4,5,6,7,8,9,10,'J','Q','K','A']:
                self.cards.append( Card(rank,Card.suits[suit]) )
        if shuffle:
            self.shuffle()

    def shuffle(self):
       random.shuffle(self.cards)

    def deal(self,cards=1):
        return [self.cards.popleft() for _ in range(cards)]



if __name__ == '__main__':
    deck = Deck()
    hand = deck.deal(5)
    print(hand)
