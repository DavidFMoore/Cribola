from Cribola import *
import unittest

class TestHand(unittest.TestCase):

    def test_perfect_hand(self):
        perfect_hand = Hand([Card(5,0), Card(5,1), Card(5,2), Card(5,3)],
                                myCrib=True)
        score = perfect_hand.total_score([Card(11,0)])
        self.assertEqual(score, 29)

    def test_no_crib_no_knobs(self):
        imperfect_hand = Hand([Card(5,0), Card(5,1), Card(5,2), Card(5,3)],
                                myCrib=False)
        score = imperfect_hand.total_score([Card(11,0)])
        self.assertEqual(score, 28)

    def test_runof4_not3(self):
        hand = Hand([Card(1,0), Card(2,1), Card(3,2), Card(4,3)])
        score = hand.total_score([Card(5,0)])
        self.assertEqual(score, 7)

    def test_flush(self):
        hand = Hand([Card(2,0), Card(4,0), Card(6,0), Card(8,0)])
        score = hand.total_score([Card(10,0)])
        self.assertEqual(score, 5)

if __name__ == "__main__":
    unittest.main()
