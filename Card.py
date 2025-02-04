class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __repr__(self):
        return f"{self.value} of {self.color}"
