@echo off
echo ========================================
echo Idle Blackjack - Rebuild Script
echo ========================================
echo.
echo Closing ALL running instances of IdleBlackjack...
taskkill /F /IM IdleBlackjack.exe /T 2>nul
echo Waiting for processes to close...
timeout /t 3 /nobreak >nul

echo.
echo Rebuilding executable with latest fixes...
echo - Fixed white backgrounds
echo - Dealer score shows in real-time
echo - New Game button is visible
echo - Improved layout and spacing
echo.
python -m PyInstaller --onefile --windowed --add-data "fonts;fonts" --add-data "images;images" --icon=NONE --name="IdleBlackjack" --clean BlackjackUI.py

echo.
echo ========================================
if errorlevel 1 (
    echo BUILD FAILED! Check error messages above.
    echo Make sure all IdleBlackjack.exe instances are closed.
) else (
    echo BUILD COMPLETE!
    echo Executable is in the dist folder.
    echo Run "Launch Blackjack.bat" to start the game.
)
echo ========================================
echo.
pause
