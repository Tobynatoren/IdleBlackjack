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

    def dealerTurn(self):
        drawnCardValue = d.dealerDraw.value(self.deck)
        if self.dealerScore < 1:
            self.dealerScore = drawnCardValue
        else:
            self.dealerScore = self.dealerScore + drawnCardValue

    def checkDealerBust(self, dealerScore):
        if dealerScore > 21:
            return True
        else:
            return False


     # Player Logic
    def playerTurn(self):
        drawnCardValue = p.playerDraw.value(deck)
        if self.playerScore < 1:
            self.playerScore = drawnCardValue
        else:
            self.playerScore = self.playerScore + drawnCardValue

    def checkPlayerBust(self):
        if self.playerScore > 21:
            return True
        else:
            return False
        
    def checkPlayerWin(self, playerScore, dealerScore):
        if playerScore > dealerScore:
            return True
        else:
            return False
        
    def checkPlayerBlackjack(self, playerScore):
        if playerScore == 21:
            return True
        else:
            return False
        
    def checkPlayerLose(self, playerScore, dealerScore):
        if playerScore < dealerScore:
            return True
        else:
            return False
        
    def checkPlayerTie(self, playerScore, dealerScore):
        if playerScore == dealerScore:
            return True
        else:
            return False
        
    def checkPlayerWinBlackjack(self, playerScore, dealerScore):
        if playerScore == 21 and dealerScore != 21:
            return True
        else:
            return False
