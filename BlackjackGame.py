import tkinter as tk
import random as r
import Card as card
import Deck as deck
import Player as p
import Dealer as d



class BlackjackGame:

    def __init__(self):
        self.dealerScore = 0
        self.playerScore = 0 
        self.deckSize = 0



    # Dealer Logic

    def dealerTurn():
        drawnCardValue = d.dealerDraw.value(deck)
        if dealerScore < 1:
            dealerScore = drawnCardValue
        else:
            dealerScore = dealerScore + drawnCardValue

    def checkDealerBust(dealerScore):
        if dealerScore > 21:
            return True
        else:
            return False


     # Player Logic
    def playerTurn():
        drawnCardValue = p.playerDraw.value(deck)
        if playerScore < 1:
            playerScore = drawnCardValue
        else:
            playerScore = playerScore + drawnCardValue

    def checkPlayerBust(playerScore):
        if playerScore > 21:
            return True
        else:
            return False