
class Board:
    """
    A class to represent one player's position on the cribbage board.
    """
    def __init__(self):
        self.position = 0

    def advance(self, score):
        """
        Advance self.position by score
        """
        self.position += score
