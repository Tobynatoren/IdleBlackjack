import random

class Card:
    suits = ['♠', '♥', '♦', '♣']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    value_map = {'A': 1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

    def __init__(self, value, suit):
        self.rank = value
        self.suit = suit
        self.value = Card.value_map[value]

    def __repr__(self):
        return f"{self.rank}{self.suit}"
