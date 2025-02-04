
import Card


class Dealer:
    def __init__(self):
        self.hand = []
        self.handValue = 0
        self.handValueAlt = 0
        self.busted = False

    def addCard(self, card):
        self.hand.append(card)
        self.handValue += card.value
        if card.rank == 'Ace':
            self.handValueAlt = self.handValue + 10

    def checkBust(self):
        if self.handValue > 21:
            self.busted = True
        if self.handValueAlt > 21:
            self.busted = True

    def checkBlackjack(self):
        if self.handValue == 21:
            return True
        else:
            return False

    def reset(self):
        self.hand = []
        self.handValue = 0
        self.handValueAlt = 0
        self.busted = False

