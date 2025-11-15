@echo off
echo ========================================
echo Creating Clean Distribution Package
echo ========================================
echo.

REM Create distribution folder
if exist "IdleBlackjack_Distribution" (
    echo Removing old distribution folder...
    rmdir /S /Q "IdleBlackjack_Distribution"
)

echo Creating new distribution folder...
mkdir "IdleBlackjack_Distribution"

echo.
echo Copying files...
echo - Copying IdleBlackjack.exe...
copy "dist\IdleBlackjack.exe" "IdleBlackjack_Distribution\" >nul

echo - Copying fonts folder...
xcopy "fonts" "IdleBlackjack_Distribution\fonts\" /E /I /Y >nul

echo - Copying images folder...
xcopy "images" "IdleBlackjack_Distribution\images\" /E /I /Y >nul

echo - Creating README for player...
(
echo IDLE BLACKJACK
echo ===============
echo.
echo HOW TO PLAY:
echo 1. Double-click IdleBlackjack.exe to start the game
echo 2. Press Ctrl+Shift+B anywhere on your computer to show/hide the game window
echo 3. Place your bet and click START GAME
echo 4. Click HIT to draw a card, STAND to end your turn
echo 5. Try to get as close to 21 without going over!
echo.
echo CONTROLS:
echo - Ctrl+Shift+B: Toggle game window on/off ^(works from anywhere!^)
echo - Click buttons to play
echo - Close the window or press the hotkey to hide it
echo.
echo BETTING:
echo - Starting balance: $1000
echo - Win: 2x your bet
echo - Blackjack: 2.5x your bet
echo - If you go broke, you get reset to $1000
echo.
echo Have fun!
) > "IdleBlackjack_Distribution\README.txt"

echo.
echo ========================================
echo Package created successfully!
echo ========================================
echo.
echo The clean distribution is in: IdleBlackjack_Distribution\
echo.
echo You can now:
echo 1. Zip the IdleBlackjack_Distribution folder
echo 2. Send it to your friend
echo 3. They just unzip and run IdleBlackjack.exe!
echo.
echo No Python installation needed - it's all standalone!
echo ========================================
pause
