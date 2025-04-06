import tkinter as tk
from tkinter import font as tkFont
from PIL import Image, ImageTk, ImageFont  # Using a Pillow library to register custom balatro font
from BlackjackGame import BlackjackGame

class BlackjackUI:
    def __init__(self):
        self.game = BlackjackGame()
        self.root = tk.Tk()
        self.root.title("Blackjack")
        self.root.geometry("400x400")
        self.root.configure(bg="#006400")

        # Load custom font
        custom_font_path = "fonts/balatro.ttf"  # Path to your font file
        custom_font = ImageFont.truetype(custom_font_path)  # Load the font with Pillow
        print(f"Loaded font family: {custom_font.getname()[0]}")  # Debugging font print to check it's loaded correctly

        # Register the font with tkinter
        self.tk_custom_font = tkFont.Font(family=custom_font.getname()[0], size=16)
        self.tk_custom_font.actual()  # Force tkinter to recognize the font

        # Loading of background - TODO: find en animated gif 
        background_image_path = "images/marble-pattern-background.jpg"  # Path to your image
        bg_image = Image.open(background_image_path)
        bg_image = bg_image.resize((400, 400))  # Resize the image to match the window size
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        # Canvas to hold the background 
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)  # Use place() to set it as the background

        # Add background image to the canvas
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Title Frame
        self.title_frame = tk.Frame(self.root, bg="#006400")
        self.title_frame.pack(pady=10)

        self.title_label = tk.Label(self.title_frame, text="Idle Blackjack", font=("balatro", 16))
        self.title_label.pack()

        # Dealer Frame
        self.dealer_frame = tk.Frame(self.root, bg="#006400")
        self.dealer_frame.pack(pady=10)

        self.dealer_label = tk.Label(self.dealer_frame, text="Dealer's Cards:", font=("balatro", 12), bg="#006400", fg="white")
        self.dealer_label.pack()

        self.dealer_cards = tk.Label(self.dealer_frame, text="", font=("balatro", 14), bg="white", width=30, height=2)
        self.dealer_cards.pack()

        # Player Frame
        self.player_frame = tk.Frame(self.root, bg="#006400")
        self.player_frame.pack(pady=10)

        self.player_label = tk.Label(self.player_frame, text="Your Cards:", font=("balatro", 12), bg="#006400", fg="white")
        self.player_label.pack()

        self.player_cards = tk.Label(self.player_frame, text="", font=("balatro", 14), bg="white", width=30, height=2)
        self.player_cards.pack()

        # Status Frame
        self.status_frame = tk.Frame(self.root, bg="#006400")
        self.status_frame.pack(pady=10)

        self.status_label = tk.Label(self.status_frame, text="Hit or Stand?", font=("balatro", 12), bg="#006400", fg="white")
        self.status_label.pack()

        # Button Frame
        self.button_frame = tk.Frame(self.root, bg="#006400")
        self.button_frame.pack(pady=10)

        self.hit_button = tk.Button(self.button_frame, text="Hit", font=("balatro", 12), command=self.hit)
        self.hit_button.grid(row=0, column=0, padx=10)

        self.stand_button = tk.Button(self.button_frame, text="Stand", font=("balatro", 12), command=self.stand)
        self.stand_button.grid(row=0, column=1, padx=10)

        #self.newgame_button = tk.Button(self.button_frame, text="New Game", font=("balatro", 12), command=self.new_game)
        #self.newgame_button.grid(row=0, column=2, padx=10)

        # New Game Button Frame (Bottom)
        self.newgame_frame = tk.Frame(self.root, bg="#006400")
        self.newgame_frame.pack(side=tk.BOTTOM, pady=10)

        self.newgame_button = tk.Button(self.newgame_frame, text="New Game", font=("balatro", 12), command=self.new_game)
        self.newgame_button.pack()

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
