from Dealer import Dealer  # Import the class
from Player import Player  # Import the class

class Game:
    def __init__(self, player):
        self.dealer = Dealer()  # Create Dealer inside the class
        self.player = player
        player = Player()
        game = Game(player)  # No need to pass a Dealer

