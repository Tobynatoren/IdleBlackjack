import random
from Card import Card  # Import the Card class

class Deck:
    def __init__(self):
        self.cards = self.create_deck()
        self.shuffle_deck()

    def create_deck(self):
        # Creates a deck of cards.
        return [Card(value, color) for value in self.values for color in self.colors]

    def shuffle_deck(self):
        # Shuffles the deck.
        random.shuffle(self.cards)

    def draw_card(self):
        # Draws a card from the deck.
        return self.cards.pop() if self.cards else None
