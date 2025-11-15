@echo off
echo ========================================
echo Testing if new version works correctly
echo ========================================
echo.
echo Starting the NEW executable from dist folder...
echo Press Ctrl+Shift+B to toggle visibility.
echo.
echo If you see white backgrounds, the OLD version is running!
echo If you see green/clean backgrounds, the NEW version is working!
echo.
pause
start "" "%~dp0dist\IdleBlackjack.exe"
