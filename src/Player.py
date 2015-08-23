from Cribola import Board

class Player:
    """
    A class for holding a player's characteristics.
        Inputs:
            - isAI : boolean, is player controlled by AI?
    """
    def __init__(self, isAI):
        self.pegs = Board()
        self.isAI = isAI
