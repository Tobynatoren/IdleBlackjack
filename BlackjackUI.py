import tkinter as tk
from tkinter import font as tkFont
from PIL import Image, ImageTk, ImageFont, ImageDraw
from BlackjackGame import BlackjackGame
from pynput import keyboard
import threading

class BlackjackUI:
    def __init__(self):
        self.game = BlackjackGame()
        self.root = tk.Tk()
        self.root.title("♠ Idle Blackjack ♥ - Press Ctrl+Shift+B to toggle")
        self.root.geometry("650x700")
        self.root.resizable(False, False)  # Disable resizing
        self.root.configure(bg="#0f1419")
        self.window_visible = True
        self.animation_running = False

        # Money system
        self.balance = 1000  # Starting balance
        self.current_bet = 10  # Default bet
        self.min_bet = 5
        self.max_bet = 100

        # Game state
        self.game_in_progress = False

        # Override window close button to hide instead of destroy
        self.root.protocol("WM_DELETE_WINDOW", self.hide_window)

        # Load custom font
        try:
            custom_font_path = "fonts/balatro.ttf"
            custom_font = ImageFont.truetype(custom_font_path)
            self.font_family = custom_font.getname()[0]
        except:
            self.font_family = "Arial"

        # Create gradient background ONCE
        self.create_gradient_background()

        # Main container with matching background
        self.main_frame = tk.Frame(self.root, bg="#0f1419", bd=0)
        self.main_frame.pack(fill="both", expand=True, padx=15, pady=5)

        # Title with glow effect
        self.title_frame = tk.Frame(self.main_frame, bg="#0f1419")
        self.title_frame.pack(pady=5)

        self.title_label = tk.Label(
            self.title_frame,
            text="♠ BLACKJACK ♥",
            font=(self.font_family, 24, "bold"),
            bg="#0f1419",
            fg="#ffd700",
            relief="flat"
        )
        self.title_label.pack()

        # Subtitle
        self.subtitle_label = tk.Label(
            self.title_frame,
            text="Place your bet to begin",
            font=(self.font_family, 10),
            bg="#0f1419",
            fg="#aaaaaa"
        )
        self.subtitle_label.pack()

        # Money Display Section
        self.create_money_section()

        # Dealer Section
        self.create_dealer_section()

        # Player Section
        self.create_player_section()

        # Status Section with animations
        self.create_status_section()

        # Buttons Section
        self.create_button_section()

        # Hotkey hint at bottom
        self.hotkey_label = tk.Label(
            self.main_frame,
            text="Press Ctrl+Shift+B anywhere to toggle window",
            font=(self.font_family, 9),
            bg="#0f1419",
            fg="#888888"
        )
        self.hotkey_label.pack(pady=5)

        # Don't deal initial cards - wait for New Game
        self.update_ui()

        # Start global hotkey listener in background thread
        self.setup_hotkey()

        self.root.mainloop()

    def create_gradient_background(self):
        """Create a rich gradient background like Balatro"""
        width = 650
        height = 700

        # Create gradient image with richer colors
        gradient = Image.new('RGB', (width, height), "#0f1419")
        draw = ImageDraw.Draw(gradient)

        for i in range(height):
            # Dark blue to purple gradient
            progress = i / height
            r = int(15 + progress * 50)  # 15 -> 65
            g = int(20 + progress * 20)  # 20 -> 40
            b = int(25 + progress * 60)  # 25 -> 85
            draw.line([(0, i), (width, i)], fill=(r, g, b))

        self.bg_photo = ImageTk.PhotoImage(gradient)
        bg_label = tk.Label(self.root, image=self.bg_photo, bd=0)
        bg_label.place(x=0, y=0, width=width, height=height)

    def create_money_section(self):
        """Create money and betting display"""
        # Balance display - always visible
        balance_container = tk.Frame(self.main_frame, bg="#3d2660", highlightbackground="#8b5cf6", highlightthickness=2)
        balance_container.pack(pady=5, padx=10, fill="x")

        self.balance_label = tk.Label(
            balance_container,
            text=f"💰 ${self.balance}",
            font=(self.font_family, 18, "bold"),
            bg="#3d2660",
            fg="#fbbf24",
            pady=5
        )
        self.balance_label.pack()

        # Betting section - will be hidden when game starts
        self.bet_container = tk.Frame(self.main_frame, bg="#1e293b", highlightbackground="#60a5fa", highlightthickness=2)
        self.bet_container.pack(pady=5, padx=10, fill="x")

        # Bet title
        tk.Label(
            self.bet_container,
            text="💵 PLACE BET",
            font=(self.font_family, 14, "bold"),
            bg="#1e293b",
            fg="#60a5fa",
            pady=5
        ).pack()

        # Bet amount display
        self.bet_label = tk.Label(
            self.bet_container,
            text=f"${self.current_bet}",
            font=(self.font_family, 32, "bold"),
            bg="#1e293b",
            fg="#fbbf24",
            pady=5
        )
        self.bet_label.pack()

        # Bet controls
        bet_controls = tk.Frame(self.bet_container, bg="#1e293b")
        bet_controls.pack(pady=5)

        self.bet_down_button = tk.Button(
            bet_controls,
            text="- $5",
            font=(self.font_family, 12, "bold"),
            bg="#dc2626",
            fg="white",
            command=self.decrease_bet,
            width=6,
            height=1,
            cursor="hand2"
        )
        self.bet_down_button.grid(row=0, column=0, padx=5)
        self.add_button_hover(self.bet_down_button, "#dc2626", "#ef4444")

        self.bet_up_button = tk.Button(
            bet_controls,
            text="+ $5",
            font=(self.font_family, 12, "bold"),
            bg="#16a34a",
            fg="white",
            command=self.increase_bet,
            width=6,
            height=1,
            cursor="hand2"
        )
        self.bet_up_button.grid(row=0, column=1, padx=5)
        self.add_button_hover(self.bet_up_button, "#16a34a", "#22c55e")

        # Quick bet buttons
        quick_bet_frame = tk.Frame(self.bet_container, bg="#1e293b")
        quick_bet_frame.pack(pady=5)

        for amount in [10, 25, 50]:
            btn = tk.Button(
                quick_bet_frame,
                text=f"${amount}",
                font=(self.font_family, 9),
                bg="#475569",
                fg="white",
                command=lambda a=amount: self.set_bet(a),
                width=4,
                cursor="hand2"
            )
            btn.pack(side="left", padx=3)
            self.add_button_hover(btn, "#475569", "#64748b")

    def increase_bet(self):
        """Increase bet amount"""
        if self.current_bet < self.max_bet and self.current_bet < self.balance:
            self.current_bet += 5
            self.bet_label.config(text=f"${self.current_bet}")
            self.animate_bet_change()

    def set_bet(self, amount):
        """Set bet to specific amount"""
        if amount <= self.balance and amount >= self.min_bet and amount <= self.max_bet:
            self.current_bet = amount
            self.bet_label.config(text=f"${self.current_bet}")
            self.animate_bet_change()

    def decrease_bet(self):
        """Decrease bet amount"""
        if self.current_bet > self.min_bet:
            self.current_bet -= 5
            self.bet_label.config(text=f"${self.current_bet}")
            self.animate_bet_change()

    def animate_bet_change(self):
        """Quick pulse animation when bet changes"""
        original_size = 32
        self.bet_label.config(font=(self.font_family, 36, "bold"))
        self.root.after(100, lambda: self.bet_label.config(font=(self.font_family, original_size, "bold")))

    def create_dealer_section(self):
        """Create dealer card display section"""
        # Dealer area - hidden until game starts
        self.dealer_container = tk.Frame(self.main_frame, bg="#312e81", highlightbackground="#818cf8", highlightthickness=2)
        self.dealer_container.pack(pady=5, padx=10, fill="x")
        self.dealer_container.pack_forget()  # Hide initially

        # Dealer header
        dealer_header = tk.Frame(self.dealer_container, bg="#312e81")
        dealer_header.pack(fill="x", padx=10, pady=5)

        tk.Label(
            dealer_header,
            text="🎩 DEALER",
            font=(self.font_family, 14, "bold"),
            bg="#312e81",
            fg="#c7d2fe"
        ).pack(side="left")

        self.dealer_score_label = tk.Label(
            dealer_header,
            text="",
            font=(self.font_family, 14, "bold"),
            bg="#312e81",
            fg="#fbbf24"
        )
        self.dealer_score_label.pack(side="right")

        # Dealer cards display
        self.dealer_cards = tk.Label(
            self.dealer_container,
            text="",
            font=(self.font_family, 18, "bold"),
            bg="#312e81",
            fg="#ffffff",
            height=2,
            pady=5
        )
        self.dealer_cards.pack(padx=10, pady=5, fill="x")

    def create_player_section(self):
        """Create player card display section"""
        # Player area - hidden until game starts
        self.player_container = tk.Frame(self.main_frame, bg="#1e3a8a", highlightbackground="#60a5fa", highlightthickness=2)
        self.player_container.pack(pady=5, padx=10, fill="x")
        self.player_container.pack_forget()  # Hide initially

        # Player header
        player_header = tk.Frame(self.player_container, bg="#1e3a8a")
        player_header.pack(fill="x", padx=10, pady=5)

        tk.Label(
            player_header,
            text="🎰 YOU",
            font=(self.font_family, 14, "bold"),
            bg="#1e3a8a",
            fg="#bfdbfe"
        ).pack(side="left")

        self.player_score_label = tk.Label(
            player_header,
            text="",
            font=(self.font_family, 14, "bold"),
            bg="#1e3a8a",
            fg="#fbbf24"
        )
        self.player_score_label.pack(side="right")

        # Player cards display
        self.player_cards = tk.Label(
            self.player_container,
            text="",
            font=(self.font_family, 18, "bold"),
            bg="#1e3a8a",
            fg="#ffffff",
            height=2,
            pady=5
        )
        self.player_cards.pack(padx=10, pady=5, fill="x")

    def create_status_section(self):
        """Create status message section"""
        self.status_container = tk.Frame(self.main_frame, bg="#1e293b", highlightbackground="#8b5cf6", highlightthickness=2)
        self.status_container.pack(pady=5, padx=10, fill="x")
        self.status_container.pack_forget()  # Hide initially

        self.status_label = tk.Label(
            self.status_container,
            text="",
            font=(self.font_family, 12, "bold"),
            bg="#1e293b",
            fg="#e0e7ff",
            height=2,
            pady=5
        )
        self.status_label.pack(padx=10, pady=5)

    def create_button_section(self):
        """Create game control buttons"""
        # Start Game button (shown when betting)
        self.start_game_button = tk.Button(
            self.main_frame,
            text="⚡ START GAME ⚡",
            font=(self.font_family, 16, "bold"),
            bg="#8b5cf6",
            fg="white",
            activebackground="#7c3aed",
            command=self.start_game,
            width=20,
            height=2,
            relief="raised",
            bd=4,
            cursor="hand2"
        )
        self.start_game_button.pack(pady=10)
        self.add_button_hover(self.start_game_button, "#8b5cf6", "#a78bfa")

        # Action buttons frame (hidden until game starts)
        self.action_container = tk.Frame(self.main_frame, bg="#0f1419")
        self.action_container.pack(pady=5)
        self.action_container.pack_forget()  # Hide initially

        action_frame = tk.Frame(self.action_container, bg="#0f1419")
        action_frame.pack()

        # Hit button
        self.hit_button = tk.Button(
            action_frame,
            text="🃏 HIT",
            font=(self.font_family, 14, "bold"),
            bg="#10b981",
            fg="white",
            activebackground="#059669",
            command=self.hit,
            width=10,
            height=2,
            relief="raised",
            bd=3,
            cursor="hand2"
        )
        self.hit_button.grid(row=0, column=0, padx=10)
        self.add_button_hover(self.hit_button, "#10b981", "#34d399")

        # Stand button
        self.stand_button = tk.Button(
            action_frame,
            text="✋ STAND",
            font=(self.font_family, 14, "bold"),
            bg="#ef4444",
            fg="white",
            activebackground="#dc2626",
            command=self.stand,
            width=10,
            height=2,
            relief="raised",
            bd=3,
            cursor="hand2"
        )
        self.stand_button.grid(row=0, column=1, padx=10)
        self.add_button_hover(self.stand_button, "#ef4444", "#f87171")

        # New Round button (shown after game ends)
        self.newgame_button = tk.Button(
            self.action_container,
            text="🔄 NEW ROUND",
            font=(self.font_family, 14, "bold"),
            bg="#f59e0b",
            fg="white",
            activebackground="#d97706",
            command=self.new_round,
            width=24,
            height=2,
            relief="raised",
            bd=3,
            cursor="hand2"
        )
        self.newgame_button.pack(pady=10)
        self.add_button_hover(self.newgame_button, "#f59e0b", "#fbbf24")

    def add_button_hover(self, button, normal_color, hover_color):
        """Add hover effect to buttons"""
        button.bind("<Enter>", lambda e: button.config(bg=hover_color))
        button.bind("<Leave>", lambda e: button.config(bg=normal_color))

    def hit(self):
        if not self.animation_running:
            self.animate_button_press(self.hit_button)
            self.game.playerTurn()
            self.flash_card_area(self.player_cards, "#90EE90")
            self.update_ui()

    def stand(self):
        if not self.animation_running:
            self.animation_running = True
            self.animate_button_press(self.stand_button)
            self.flash_status("Dealer's turn...", "#FFA500")
            self.hit_button.config(state="disabled")
            self.stand_button.config(state="disabled")
            self.bet_up_button.config(state="disabled")
            self.bet_down_button.config(state="disabled")
            self.root.after(800, self.dealer_draw_step)

    def dealer_draw_step(self):
        if self.game.get_hand_value(self.game.dealer.hand) < 17:
            self.game.dealerTurn()
            self.flash_card_area(self.dealer_cards, "#FFB6C1")
            self.update_ui(dealer_revealing=True)  # Show all dealer cards as they draw
            self.root.after(800, self.dealer_draw_step)
        else:
            self.update_ui(final=True)
            self.process_bet_outcome()
            self.hit_button.config(state="normal")
            self.stand_button.config(state="normal")
            self.bet_up_button.config(state="normal")
            self.bet_down_button.config(state="normal")
            self.animation_running = False

    def start_game(self):
        """Start a new game after placing bet"""
        # Check if player has enough money
        if self.balance < self.current_bet:
            self.subtitle_label.config(text="Not enough money! Lower your bet.", fg="#ef4444")
            if self.balance < self.min_bet:
                # Game over - reset balance
                self.balance = 1000
                self.balance_label.config(text=f"💰 ${self.balance}")
                self.subtitle_label.config(text="Bankrupt! Balance reset to $1000", fg="#f59e0b")
            return

        self.animate_button_press(self.start_game_button)

        # Deduct bet with animation
        self.balance -= self.current_bet
        self.animate_balance_change()

        # Start new game
        self.game = BlackjackGame()
        self.game.dealerTurn()  # Dealer gets one card
        self.game.playerTurn()  # Player gets one card automatically
        self.game_in_progress = True

        # Hide betting UI, show game UI
        self.bet_container.pack_forget()
        self.start_game_button.pack_forget()
        self.dealer_container.pack(pady=5, padx=10, fill="x")
        self.player_container.pack(pady=5, padx=10, fill="x")
        self.status_container.pack(pady=5, padx=10, fill="x")
        self.action_container.pack(pady=5)

        # Re-enable hit/stand buttons for new game
        self.hit_button.config(state="normal")
        self.stand_button.config(state="normal")

        self.subtitle_label.config(text=f"Bet: ${self.current_bet} | Good luck!", fg="#22c55e")
        self.update_ui()
        self.animation_running = False

    def new_round(self):
        """Start a new round (return to betting)"""
        self.animate_button_press(self.newgame_button)
        self.game_in_progress = False

        # Hide game UI, show betting UI
        self.dealer_container.pack_forget()
        self.player_container.pack_forget()
        self.status_container.pack_forget()
        self.action_container.pack_forget()
        self.bet_container.pack(pady=5, padx=10, fill="x")
        self.start_game_button.pack(pady=10)

        self.subtitle_label.config(text="Place your bet to begin", fg="#aaaaaa")
        self.animation_running = False

    def animate_balance_change(self):
        """Animate balance changing"""
        self.balance_label.config(text=f"💰 ${self.balance}", font=(self.font_family, 20, "bold"))
        self.root.after(200, lambda: self.balance_label.config(font=(self.font_family, 18, "bold")))

    def process_bet_outcome(self):
        """Process the bet result and update balance"""
        outcome = self.game.checkPlayerOutcome()

        # Disable hit/stand buttons after game ends
        self.hit_button.config(state="disabled")
        self.stand_button.config(state="disabled")

        if "Blackjack" in outcome and "Dealer Blackjack" not in outcome:
            # Blackjack pays 3:2
            winnings = int(self.current_bet * 2.5)
            self.balance += winnings
            profit = winnings - self.current_bet
            self.flash_status(f"🎉 {outcome}! Won ${profit}! 🎉", "#22c55e")
            self.animate_win(profit)
        elif "Win" in outcome or "Dealer Busts" in outcome:
            # Regular win pays 2:1
            winnings = self.current_bet * 2
            self.balance += winnings
            profit = winnings - self.current_bet
            self.flash_status(f"🎉 {outcome}! Won ${profit}! 🎉", "#22c55e")
            self.animate_win(profit)
        elif "Tie" in outcome or "Push" in outcome:
            # Return bet on tie
            self.balance += self.current_bet
            self.flash_status(f"🤝 {outcome} - Bet returned", "#f59e0b")
        else:
            # Loss - bet already deducted
            self.flash_status(f"😔 {outcome} - Lost ${self.current_bet}", "#ef4444")

        self.animate_balance_change()

        # Check if player is broke
        if self.balance < self.min_bet:
            self.balance = 1000
            self.animate_balance_change()
            self.root.after(2000, lambda: self.subtitle_label.config(text="Bankrupt! Balance reset to $1000", fg="#f59e0b"))

    def animate_win(self, amount):
        """Show floating win amount"""
        # Simple implementation - could be enhanced with canvas later
        pass

    def animate_button_press(self, button):
        """Animate button press"""
        original_relief = button.cget("relief")
        button.config(relief="sunken")
        self.root.after(100, lambda: button.config(relief=original_relief))

    def flash_card_area(self, widget, color):
        """Flash animation for card area"""
        original_bg = widget.cget("bg")
        widget.config(bg=color)
        self.root.after(150, lambda: widget.config(bg=original_bg))

    def flash_status(self, message, color):
        """Animated status message with color"""
        original_fg = self.status_label.cget("fg")
        self.status_label.config(text=message, fg=color)

        # Pulse animation
        def pulse(scale, direction):
            if scale <= 0 or scale > 5:
                self.status_label.config(fg=original_fg)
                return

            brightness = 1.0 + (scale * 0.1)
            if direction == "up" and scale < 5:
                self.root.after(50, lambda: pulse(scale + 1, "up"))
            elif direction == "up":
                self.root.after(50, lambda: pulse(scale - 1, "down"))
            else:
                self.root.after(50, lambda: pulse(scale - 1, "down"))

        pulse(1, "up")

    def setup_hotkey(self):
        """Set up global hotkey listener for Ctrl+Shift+B"""
        def on_activate():
            # Use root.after to safely call toggle from the hotkey thread
            self.root.after(0, self.toggle_window)

        # Define the hotkey combination (Ctrl+Shift+B)
        hotkey = keyboard.HotKey(
            keyboard.HotKey.parse('<ctrl>+<shift>+b'),
            on_activate
        )

        def for_canonical(f):
            return lambda k: f(listener.canonical(k))

        # Start listener in a daemon thread so it closes with the app
        listener = keyboard.Listener(
            on_press=for_canonical(hotkey.press),
            on_release=for_canonical(hotkey.release)
        )
        listener.daemon = True
        listener.start()

    def toggle_window(self):
        """Toggle window visibility"""
        if self.window_visible:
            self.hide_window()
        else:
            self.show_window()

    def hide_window(self):
        """Hide the window"""
        self.root.withdraw()
        self.window_visible = False

    def show_window(self):
        """Show the window"""
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()
        self.window_visible = True

    def update_ui(self, final=False, dealer_revealing=False):
        player_score = self.game.get_hand_value(self.game.player.hand)
        dealer_score = self.game.get_hand_value(self.game.dealer.hand)

        # Player display
        player_cards_text = "  ".join(map(str, self.game.player.hand))
        self.player_cards.config(text=player_cards_text if player_cards_text else "Click NEW GAME to start")
        self.player_score_label.config(text=f"Score: {player_score}" if self.game.player.hand else "")

        # Dealer display
        if final or dealer_revealing:
            # Show all cards and full score (final or during dealer's turn)
            dealer_cards_text = "  ".join(map(str, self.game.dealer.hand))
            self.dealer_cards.config(text=dealer_cards_text)
            self.dealer_score_label.config(text=f"Score: {dealer_score}")
        else:
            if self.game.dealer.hand:
                # Show first card, hide rest, and show ONLY visible card's value
                hidden_cards = "  🂠" * (len(self.game.dealer.hand) - 1) if len(self.game.dealer.hand) > 1 else ""
                dealer_cards_text = f"{self.game.dealer.hand[0]}{hidden_cards}"
                self.dealer_cards.config(text=dealer_cards_text)

                # Calculate and show only the visible card's value
                visible_card_value = self.game.dealer.hand[0].value
                # Handle Ace display (show both possible values)
                if self.game.dealer.hand[0].rank == 'A':
                    self.dealer_score_label.config(text=f"Showing: {visible_card_value} or 11")
                else:
                    self.dealer_score_label.config(text=f"Showing: {visible_card_value}")
            else:
                self.dealer_cards.config(text="Click NEW GAME to start")
                self.dealer_score_label.config(text="")

        # Status - only show during play, final outcome shown in process_bet_outcome
        if not final:
            if player_score > 21:
                self.flash_status("💥 BUST! You went over 21!", "#FF0000")
                self.hit_button.config(state="disabled")
                self.stand_button.config(state="disabled")
                self.bet_up_button.config(state="normal")
                self.bet_down_button.config(state="normal")
                # Auto-process loss
                self.root.after(1500, self.auto_process_bust)
            elif player_score == 21:
                self.status_label.config(text="🎯 Perfect 21! Hit or Stand?", fg="#00FF00")
            else:
                self.status_label.config(text=f"Your score: {player_score} | Hit or Stand?", fg="#FFFFFF")

    def auto_process_bust(self):
        """Auto-process when player busts"""
        if self.game.get_hand_value(self.game.player.hand) > 21:
            # Player busted - don't need to play dealer's hand
            outcome = self.game.checkPlayerOutcome()
            self.flash_status(f"😔 {outcome} - Lost ${self.current_bet}", "#FF4444")
            # Balance already deducted, no need to process further

if __name__ == "__main__":
    BlackjackUI()
