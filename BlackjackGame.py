import Deck
import Dealer as d
import Player as p

class BlackjackGame:
    def __init__(self):
        self.deck = Deck.Deck()
        self.dealer = d.Dealer()
        self.player = p.Player()

    def playerTurn(self):
        return self.player.draw(self.deck)

    def dealerTurn(self):
        return self.dealer.draw(self.deck)

    def get_hand_value(self, hand):
        return sum(card.value for card in hand)

    def checkPlayerOutcome(self):
        player_score = self.get_hand_value(self.player.hand)
        dealer_score = self.get_hand_value(self.dealer.hand)

        if player_score > 21:
            return "Bust"
        elif player_score == 21:
            return "Blackjack"
        elif dealer_score > 21:
            return "Dealer Busts! You Win"
        elif player_score > dealer_score:
            return "Win"
        elif player_score == dealer_score:
            return "Tie"
        else:
            return "Lose"
