
class Round:
    """
    A single hand of cribbage.
    Inputs:
        - Deck : A cribbage deck object
        - P1 : A cribbage player object corresponding to player 1
        - P2 : A cribbage player object corresponding to player 2
        - whose_crib : Boolean, who gets the crib?
                False (0) = player 1, True (1) =  player 2
    """
    def __init__(self, deck, P1, P2, crib):
        deck.shuffle()
        self.players = [P1, P2]
        self.whose_crib = crib
        self.hands = [ Hand(deck.draw(6), mycrib = crib),
                       Hand(deck.draw(6), mycrib = not crib) ]
        self.upcard = deck.draw(1)
        self.crib = []

    def discard_crib(self):
        pass

    def peg(self):
        pass

    def score_hands(self):
        # score the two players' hands
        for i in range(2):
            player = ( self.whose_crib + i ) % 2
            score = self.hands[player].score(self.upcard)
            self.players[player].pegs.advance(score)
        # score the crib
        crib_score = Hand(self.crib, self.upcard, mycrib=False).score()
        self.players[self.whose_crib].pegs.advance(crib_score)
