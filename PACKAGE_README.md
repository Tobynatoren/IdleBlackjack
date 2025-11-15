# Idle Blackjack - Distribution Package

This file explains how to create a clean distribution package to send to your friend.

## What to Include

Your friend only needs these files:
1. **IdleBlackjack.exe** - The main executable (from the `dist` folder)
2. **fonts/** folder - Contains the custom font
3. **images/** folder - Contains card images and backgrounds
4. **README_FOR_PLAYER.txt** - Simple instructions for your friend

## How to Create the Package

1. Create a new folder called `IdleBlackjack_Game`
2. Copy these items into it:
   - `dist/IdleBlackjack.exe` → `IdleBlackjack_Game/IdleBlackjack.exe`
   - `fonts/` folder → `IdleBlackjack_Game/fonts/`
   - `images/` folder → `IdleBlackjack_Game/images/`
   - Create a simple README (see template below)

3. Zip the `IdleBlackjack_Game` folder
4. Send the zip file to your friend
5. They just unzip it and run IdleBlackjack.exe

## Simple README Template for Your Friend

```
IDLE BLACKJACK
===============

HOW TO PLAY:
1. Double-click IdleBlackjack.exe to start the game
2. Press Ctrl+Shift+B anywhere on your computer to show/hide the game window
3. Place your bet and click START GAME
4. Click HIT to draw a card, STAND to end your turn
5. Try to get as close to 21 without going over!

CONTROLS:
- Ctrl+Shift+B: Toggle game window on/off (works from anywhere!)
- Click buttons to play
- Close the window or press the hotkey to hide it

BETTING:
- Starting balance: $1000
- Win: 2x your bet
- Blackjack: 2.5x your bet
- If you go broke, you get reset to $1000

Have fun!
```

## What NOT to Include

DO NOT include these files (they're only for development):
- *.py files (Python source code)
- *.spec files
- *.bat files
- build/ folder
- __pycache__/ folders
- .git/ folder
- requirements.txt
- Any .md files

Your friend doesn't need Python installed - the .exe is standalone!
