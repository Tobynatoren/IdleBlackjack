import random


class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

        colors = ['red', 'black']
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

        def create_deck():
            # Create a deck of cards
            deck = [Card(value, color) for value in range(1, 14) for color in colors]

            return deck

        def shuffle_deck(deck):
            # Shuffle the deck
            random.shuffle(deck)

            return deck