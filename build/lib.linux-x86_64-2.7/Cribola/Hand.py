from Cribola import *
from itertools import combinations
from numpy import diff

class Hand:
    """
    A class for holding a 6, 4, or 4+1 card hand. Calculates the score for 4+1 card hand.
    Inputs:
        list_of_cards: List of Card objects
        myCrib: boolean value to see if in the current hand, this
                player scores points from the crib.
    """
    def __init__(self, list_of_cards, myCrib=True):
        self.cards = list_of_cards
        self.score = 0
        self.myCrib = myCrib

    def __str__(self):
        rtnstr = ""
        for c in self.cards:
            rtnstr += "%s,"%c
        return rtnstr[:-1]

    def total_score(self, fifth_card, verbose=False):
        """
        Find the total score of your 5-card hand.
        Input:
            fifth_card: length-1 list of Card objects (pulled from Deck.draw())
            verbose: print how the scores are calculated
        """
        self.cards.append(fifth_card[0])
        self.verbose = verbose

        self.find_knobs()
        self.count_fifteens()
        self.count_pairs()
        self.count_flush()
        self.count_runs()

        return self.score

    def find_knobs(self):
        """
        Add one to score if the hand has knobs
        """
        knob_suit = self.cards[-1].suit
        knobs = Card(11, knob_suit)
        if self.myCrib:
            if knobs in self.cards:
                if self.verbose: print "Knobs: +1"
                self.score += 1
        else:
            if knobs in self.cards[:-1]:
                if self.verbose: print "Knobs: +1"
                self.score += 1

    def count_fifteens(self):
        """
        Count the number of fifteens in a hand
        """
        N15 = 0 # the number of 15s.
        for Ni in range(2,6):
            N15 += self._count15N(Ni)
        if N15 > 0:
            if self.verbose: print "Fifteen x %d: +%d"%(N15, N15*2)
        self.score += N15*2

    def _count15N(self, N):
        """
        Count the number of fifteens in all permutations of N cards
        """
        val_list = [c.value for c in self.cards]
        combos = list(combinations(val_list, N))
        adds2fifteen = map( lambda x: sum(x) == 15, combos)
        return sum(adds2fifteen)

    def count_pairs(self):
        """
        count the number of pairs in the hand
        """
        pip_list = [c.pips for c in self.cards]
        combos = list(combinations(pip_list, 2))
        ispair = map( lambda (x,y): x == y, combos)
        Npairs = sum(ispair)
        if Npairs > 0 and self.verbose:
            print "Pair x %d: +%d"%(Npairs, Npairs*2)
        self.score += 2*Npairs

    def count_flush(self):
        """
        Add 4 to score if flush of 4, 5 if flush of 5
        """
        suit = self.cards[0].suit
        for i in range(1, 4):
            if not (self.cards[i].suit == suit):
                return

        if self.cards[-1].suit == suit:
            if self.verbose: print "Flush of 5: +5"
            self.score += 5
        else:
            if self.verbose: print "Flush of 4: +4"
            self.score += 4

    def count_runs(self):
        """
        Count the number of runs in a hand. Go backwards from runs of 5 to
            runs of 3 --- if we count a run of length N, return so there is
            no double counting runs of length N-1.
        """
        list_of_pips = [c.pips for c in self.cards]
        for Ncards in range(5,2,-1):
            Nruns = 0
            combos = list(combinations(list_of_pips, Ncards))
            for c in combos:
                if all( diff(sorted(c)) == 1):
                    Nruns += 1
            if Nruns > 0:
                if self.verbose:
                    print "Run of %d x %d: +%d"%(Ncards, Nruns, Ncards*Nruns)
                self.score += Ncards*Nruns
                return
