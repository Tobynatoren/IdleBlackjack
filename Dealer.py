
from Card import Card
from Deck import Deck


class Dealer:
    def __init__(self):
        self.hand = []
        self.handValue = 0
        self.handValueAlt = 0
        self.busted = False


    def dealerDraw(deck):
        return Deck.draw_card()
    
