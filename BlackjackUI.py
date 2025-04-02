import tkinter as tk
from BlackjackGame import BlackjackGame

class BlackjackUI:
    def __init__(self):
        self.game = BlackjackGame()
        self.root = tk.Tk()
        self.root.title("Blackjack")
        self.root.geometry("400x400")
        self.root.configure(bg="#006400")

        # Dealer Frame
        self.dealer_frame = tk.Frame(self.root, bg="#006400")
        self.dealer_frame.pack(pady=10)

        self.dealer_label = tk.Label(self.dealer_frame, text="Dealer's Cards:", font=("Arial", 12), bg="#006400", fg="white")
        self.dealer_label.pack()

        self.dealer_cards = tk.Label(self.dealer_frame, text="", font=("Arial", 14), bg="white", width=30, height=2)
        self.dealer_cards.pack()

        # Player Frame
        self.player_frame = tk.Frame(self.root, bg="#006400")
        self.player_frame.pack(pady=10)

        self.player_label = tk.Label(self.player_frame, text="Your Cards:", font=("Arial", 12), bg="#006400", fg="white")
        self.player_label.pack()

        self.player_cards = tk.Label(self.player_frame, text="", font=("Arial", 14), bg="white", width=30, height=2)
        self.player_cards.pack()

        # Status Frame
        self.status_frame = tk.Frame(self.root, bg="#006400")
        self.status_frame.pack(pady=10)

        self.status_label = tk.Label(self.status_frame, text="Hit or Stand?", font=("Arial", 12), bg="#006400", fg="white")
        self.status_label.pack()

        # Button Frame
        self.button_frame = tk.Frame(self.root, bg="#006400")
        self.button_frame.pack(pady=10)

        self.hit_button = tk.Button(self.button_frame, text="Hit", font=("Arial", 12), command=self.hit)
        self.hit_button.grid(row=0, column=0, padx=10)

        self.stand_button = tk.Button(self.button_frame, text="Stand", font=("Arial", 12), command=self.stand)
        self.stand_button.grid(row=0, column=1, padx=10)

        self.newgame_button = tk.Button(self.button_frame, text="New Game", font=("Arial", 12), command=self.new_game)
        self.newgame_button.grid(row=0, column=2, padx=10)

        # Initial dealer card
        self.game.dealerTurn()

        self.root.mainloop()

    def hit(self):
        self.game.playerTurn()
        self.update_ui()

    def stand(self):
        self.status_label.config(text="Dealer's turn...")
        self.root.after(500, self.dealer_draw_step)

    def dealer_draw_step(self):
        if self.game.get_hand_value(self.game.dealer.hand) < 17:
            self.game.dealerTurn()
            self.update_ui()
            self.root.after(500, self.dealer_draw_step) 
        else:
            self.update_ui(final=True)

    def new_game(self):
        self.game = BlackjackGame()
        self.game.dealerTurn()
        self.status_label.config(text="New game started! Hit or Stand?")
        self.update_ui()

    def update_ui(self, final=False):
        player_score = self.game.get_hand_value(self.game.player.hand)
        dealer_score = self.game.get_hand_value(self.game.dealer.hand)

        # Player display
        self.player_cards.config(text=f"({player_score}) " + " | ".join(map(str, self.game.player.hand)))

        # Dealer display
        if final:
            dealer_hand_display = f"({dealer_score}) " + " | ".join(map(str, self.game.dealer.hand))
        else:
            if self.game.dealer.hand:
                dealer_hand_display = f"(?) {self.game.dealer.hand[0]} | ??"
            else:
                dealer_hand_display = "(?) ??"

        self.dealer_cards.config(text=dealer_hand_display)

        # Status
        if final:
            outcome = self.game.checkPlayerOutcome()
            self.status_label.config(text=f"{outcome} | Your: {player_score} | Dealer: {dealer_score}")
        else:
            if player_score > 21:
                self.status_label.config(text=f"Bust! You went over 21.")
            else:
                self.status_label.config(text=f"Your score: {player_score} | Hit or Stand?")

if __name__ == "__main__":
    BlackjackUI()
