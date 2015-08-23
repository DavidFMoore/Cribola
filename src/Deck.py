from Cribola import *
from random import shuffle

class Deck:
    """
    A class for describing a deck of 52 poker cards
    """
    def __init__(self):
        self.cards = []
        self.topcard = 0
        for pips in range(1,14):
            for suit in range(4):
                self.cards.append(Card(pips, suit))

    def __getitem__(self, arg):
        return self.cards[arg]

    def shuffle(self):
        """
        Randomly rearrange the order of the cards, return self.topcard to zero
        """
        shuffle(self.cards)
        self.topcard = 0

    def draw(self, N):
        """
        Returns cards topcard to topcard+N of deck.cards
        """
        cards2deal = self.cards[self.topcard : self.topcard+N]
        self.topcard += N
        return cards2deal
