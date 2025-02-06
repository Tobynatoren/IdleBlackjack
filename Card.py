import random
class Card:




    colors = ['red', 'black']
    values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']


    def __init__(self, value, color):
        
        self.value = random.choice(Card.values)
        self.color = random.choice(Card.colors)

    def __repr__(self):
        return f"{self.value} of {self.color}"