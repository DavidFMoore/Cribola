from Cribola import Deck, Card
import unittest

def equal_cards(listocards1, listocards2):
    rtnval = True
    for c1,c2 in zip(listocards1, listocards2):
        #print "%s %s"%(c1, c2)
        rtnval &= c1 == c2
    return rtnval

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_getitem(self):
        """
        __getitem__ gets the indicated card (relies on unshuffled order
            of initial deck)
        """
        shouldbe_card = Card(1,0)
        self.assertTrue(shouldbe_card, self.deck[0])

    def test_draw(self):
        """
        draw(n) returns the first n cards in the deck
        """
        shouldbe_cards = [Card(1,0), Card(1,1)]
        self.assertTrue(equal_cards(shouldbe_cards, self.deck.draw(2)))

    def test_draw2(self):
        """
        two successive calls of draw(n) return the top 2n cards of the deck.
        """
        shouldbe = [Card(1,0), Card(1,1)]
        draw1 = self.deck.draw(1)
        draw2 = self.deck.draw(2)
        for c in draw2:
            draw1.append(c)
        self.assertTrue(equal_cards(shouldbe, draw1))

if __name__ == "__main__":
    unittest.main()
