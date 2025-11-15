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
        """Calculate the best value for a hand, treating Aces as 1 or 11"""
        total = sum(card.value for card in hand)
        aces = sum(1 for card in hand if card.rank == 'A')

        # Try to use Aces as 11 if it doesn't bust
        while aces > 0 and total + 10 <= 21:
            total += 10
            aces -= 1

        return total

    def is_blackjack(self, hand):
        """Check if hand is a natural blackjack (21 with 2 cards)"""
        return len(hand) == 2 and self.get_hand_value(hand) == 21

    def checkPlayerOutcome(self):
        player_score = self.get_hand_value(self.player.hand)
        dealer_score = self.get_hand_value(self.dealer.hand)
        player_blackjack = self.is_blackjack(self.player.hand)
        dealer_blackjack = self.is_blackjack(self.dealer.hand)

        if player_score > 21:
            return "Bust"
        elif player_blackjack and dealer_blackjack:
            return "Both Blackjack! Tie"
        elif player_blackjack:
            return "Blackjack! You Win"
        elif dealer_blackjack:
            return "Dealer Blackjack! You Lose"
        elif dealer_score > 21:
            return "Dealer Busts! You Win"
        elif player_score > dealer_score:
            return "Win"
        elif player_score == dealer_score:
            return "Tie"
        else:
            return "Lose"
