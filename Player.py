class Player:
    def __init__(self):
        self.hand = []

    def draw(self, deck):
        card = deck.draw_card()
        if card:
            self.hand.append(card)
        return card
