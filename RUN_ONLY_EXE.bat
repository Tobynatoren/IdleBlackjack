@echo off
echo ========================================
echo IMPORTANT: This runs ONLY the .exe file
echo NOT the Python source code!
echo ========================================
echo.
echo Step 1: Killing ALL old instances...
echo (This is CRITICAL - old instances hijack the hotkey!)
echo.
taskkill /F /IM IdleBlackjack.exe /T 2>nul
taskkill /F /IM python.exe /FI "WINDOWTITLE eq Blackjack*" 2>nul
taskkill /F /IM pythonw.exe 2>nul

echo Waiting 3 seconds for processes to fully close...
timeout /t 3 /nobreak >nul

echo.
echo Step 2: Verifying all instances are closed...
tasklist /FI "IMAGENAME eq IdleBlackjack.exe" 2>NUL | find /I /N "IdleBlackjack.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo WARNING: Some instances still running! Trying again...
    taskkill /F /IM IdleBlackjack.exe /T 2>nul
    timeout /t 2 /nobreak >nul
)

echo.
echo Step 3: Starting the NEW .exe from dist folder...
echo.
cd /d "%~dp0"
start "" "%~dp0dist\IdleBlackjack.exe"

echo.
echo ========================================
echo TESTING CHECKLIST:
echo ========================================
echo 1. Do you see WHITE backgrounds? = OLD VERSION (BAD!)
echo 2. Do you see light GREEN backgrounds? = NEW VERSION (GOOD!)
echo 3. Press Ctrl+Shift+B to test the hotkey
echo 4. Does "Dealer: Showing: X" appear? = NEW VERSION (GOOD!)
echo.
echo If you see the OLD version, close EVERYTHING and run this again!
echo ========================================
echo.
pause
