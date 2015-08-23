
class Card:
    """
    A class for describing a poker card.
    inputs:
        pips: an int from 1-13 (ace to king)
        suit: an int from 1-4 (spades, clubs, hearts, diamonds)
    """
    def __init__(self, pips, suit):
        self.pips  = pips
        self.value = pips if pips < 10 else 10
        self.suit  = suit

    def __str__(self):
        suits  = 'SCHD'
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K' ]
        return "%s%s"%(values[self.pips-1], suits[self.suit])

    def __eq__(self, card2):
        return (self.pips == card2.pips) and (self.suit == card2.suit)
