import unittest
from Cribola import Card

class TestCard(unittest.TestCase):

    def setUp(self):
        pass

    def test_value_number(self):
        """
        Value of a numbered card should be equal to the number of pips.
        """
        c = Card(9,1)
        self.assertEqual( c.value, c.pips)

    def test_value_tenner(self):
        """
        Value of a face card should be ten.
        """
        c = Card(11,0)
        self.assertEqual(c.value, 10)

    def test_string(self):
        """
        String should read as face+suit
        """
        c = Card(11,0)
        cstr = "%s"%c
        self.assertEqual( cstr, "JS")

    def test_equality(self):
        """
        Equality function should choose cards with same pips+suit
        """
        c1 = Card(11,0)
        c2 = Card(11,0)
        eq_return = c1 == c2
        self.assertTrue(eq_return)

    def test_inequality(self):
        """
        Equality function should return false if pips or suit is different
        """
        c1 = Card(11,0)
        c2 = Card(11,1)
        self.assertFalse(c1 == c2)

if __name__ == '__main__':
    unittest.main()
