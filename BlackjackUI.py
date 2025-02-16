import tkinter as tk
from BlackjackGame import BlackjackGame

class BlackjackUI:
    def __init__(self):
        self.game = BlackjackGame()  # Create an instance of the game logic

        # UI
        self.root = tk.Tk()
        self.root.title("Blackjack")
        self.root.geometry("400x400")
        self.root.configure(bg="#006400")  # Dark green background

        # Dealer's cards display
        self.dealer_frame = tk.Frame(self.root, bg="#006400")
        self.dealer_frame.pack(pady=10)

        self.dealer_label = tk.Label(self.dealer_frame, text="Dealer's Cards:", font=("Arial", 12), bg="#006400", fg="white")
        self.dealer_label.pack()

        self.dealer_cards = tk.Label(self.dealer_frame, text="?? ??", font=("Arial", 14), bg="white", width=20, height=2)
        self.dealer_cards.pack()

        # Player's cards display
        self.player_frame = tk.Frame(self.root, bg="#006400")
        self.player_frame.pack(pady=10)

        self.player_label = tk.Label(self.player_frame, text="Your Cards:", font=("Arial", 12), bg="#006400", fg="white")
        self.player_label.pack()

        self.player_cards = tk.Label(self.player_frame, text="?? ??", font=("Arial", 14), bg="white", width=20, height=2)
        self.player_cards.pack()

        # Game status text display
        self.status_frame = tk.Frame(self.root, bg="#006400")
        self.status_frame.pack(pady=10)

        self.status_label = tk.Label(self.status_frame, text="Hit or Stand?", font=("Arial", 12), bg="#006400", fg="white")
        self.status_label.pack()

        # Buttons
        self.button_frame = tk.Frame(self.root, bg="#006400")
        self.button_frame.pack(pady=10)

        self.hit_button = tk.Button(self.button_frame, text="Hit", font=("Arial", 12), command=self.hit)
        self.hit_button.grid(row=0, column=0, padx=10)

        self.stand_button = tk.Button(self.button_frame, text="Stand", font=("Arial", 12), command=self.stand)
        self.stand_button.grid(row=0, column=1, padx=10)

        self.root.mainloop()

    def hit(self):
        self.game.playerTurn()
        self.update_ui()

    def stand(self):
        self.game.dealerTurn()
        self.update_ui()

    def update_ui(self):
        # Update the UI elements based on the game state
        self.player_cards.config(text=f"Player Score: {self.game.playerScore}")
        self.dealer_cards.config(text=f"Dealer Score: {self.game.dealerScore}")
        outcome = self.game.checkPlayerOutcome()
        self.status_label.config(text=outcome)

# Run the game
if __name__ == "__main__":
    BlackjackUI()