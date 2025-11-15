# Idle Blackjack

A beautiful, animated blackjack game for quick play while waiting! Features a modern UI with smooth animations, betting system, and global hotkey support.

## Features

### Betting System 💰
- **Starting Balance**: Begin with $1,000
- **Flexible Betting**: Bet between $5 and $100
- **Realistic Payouts**:
  - Blackjack: 3:2 payout (bet $10, win $15)
  - Regular Win: 2:1 payout (bet $10, win $10)
  - Tie/Push: Bet returned
  - Loss: Lose your bet
- **Bankruptcy Protection**: Auto-reset to $1,000 if you go broke
- **Easy Bet Controls**: Use ◀ ▶ buttons to adjust bet amount

### Improved Blackjack Logic
- **Smart Ace Handling**: Aces automatically count as 1 or 11, whichever benefits you more
- **True Blackjack Detection**: Natural blackjack (21 with 2 cards) is now properly recognized
- **Realistic Dealer Behavior**: Dealer draws until reaching 17 or higher

### Modern UI Design
- **Gradient Background**: Smooth green gradient for a casino-like feel
- **Color-Coded Sections**: Clear separation between dealer, player, and money areas with golden borders
- **Large, Readable Display**: Cards and scores shown prominently
- **Prominent New Game Button**: Large yellow button that's easy to find
- **Emoji Indicators**: Fun visual cues for game state

### Smooth Animations
- **Button Press Animations**: Visual feedback when clicking buttons
- **Card Flash Effects**: Cards flash when drawn (green for player, pink for dealer)
- **Status Pulse**: Important messages pulse with color
- **Hover Effects**: Buttons change color on hover for better interactivity
- **Money Updates**: Balance animates when you win or lose

### Global Hotkey
- **Ctrl+Shift+B**: Toggle the game window from anywhere
- Perfect for quick gaming sessions while waiting for game lobbies to load
- Window hides instead of closing, so you can instantly bring it back

## How to Use

### Option 1: Run the Executable (Easiest)
1. **Close any running instances** of the game first
2. Double-click **`Rebuild.bat`** to create the latest executable (only needed after updates)
3. Or double-click **`Launch Blackjack.bat`** to start the game
4. Or navigate to the `dist` folder and run `IdleBlackjack.exe`
5. Press **Ctrl+Shift+B** from anywhere to show/hide the game

### Option 2: Run from Source
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the game:
   ```bash
   python BlackjackUI.py
   ```

## Controls

### Money & Betting
- **◀ Button**: Decrease bet by $5
- **▶ Button**: Increase bet by $5
- **💰 Balance**: Shows your current money
- **💵 Bet**: Shows your current bet amount
- Adjust bet BEFORE clicking New Game
- Bet controls disabled during active games

### In-Game Buttons
- **🃏 HIT** (Green): Draw another card
- **✋ STAND** (Red): Stop drawing and let the dealer play
- **🔄 NEW GAME** (Yellow): Start a fresh round and place your bet

### Global Hotkey
- **Ctrl+Shift+B**: Show/hide the game window from anywhere

### Window Controls
- **X Button**: Hides the window (doesn't close the app)
- Game continues running in background for instant access

## Game Rules

1. **Objective**: Get closer to 21 than the dealer without going over
2. **Card Values**:
   - Number cards: Face value
   - Face cards (J, Q, K): 10 points
   - Aces: 1 or 11 (automatically calculated for best value)
3. **Winning**:
   - Natural Blackjack: 21 with first 2 cards (pays 3:2)
   - Higher score than dealer without busting (pays 2:1)
   - Dealer busts (goes over 21) (pays 2:1)
4. **Losing**:
   - You bust (go over 21)
   - Dealer has higher score
   - Dealer has natural blackjack
5. **Push (Tie)**:
   - Same score as dealer
   - Your bet is returned

## Color Guide

- **🟢 Green Status**: You won or have good standing
- **🔴 Red Status**: You lost or busted
- **🟠 Orange Status**: Tie/Push
- **🟡 Gold**: Titles and important information

## Building the Executable

### Easy Method:
1. Close any running instances of IdleBlackjack.exe
2. Double-click **`Rebuild.bat`**
3. Wait for the build to complete
4. Find the new executable in the `dist` folder

### Manual Method:
If you make changes and want to rebuild the .exe manually:

```bash
python -m PyInstaller --onefile --windowed --add-data "fonts;fonts" --add-data "images;images" --name="IdleBlackjack" --clean BlackjackUI.py
```

The new executable will be in the `dist` folder.

**Note**: If you get a "Permission Denied" error, make sure to close the game first!

## Requirements

- Python 3.7+
- Pillow (for images and custom fonts)
- pynput (for global hotkeys)
- tkinter (usually included with Python)

## Tips

- Use the hotkey feature to keep the game running in background
- Perfect for loading screens, compilation times, or short breaks
- The game remembers your current hand when hidden
- Buttons are disabled during dealer's turn to prevent misclicks

Enjoy your quick blackjack sessions! 🎰♠♥♦♣
