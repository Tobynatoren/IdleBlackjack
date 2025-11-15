@echo off
echo Forcefully closing ALL IdleBlackjack instances...
echo.

REM Kill by process name
taskkill /F /IM "IdleBlackjack.exe" /T 2>nul

REM Wait a moment
timeout /t 2 /nobreak >nul

REM Check if any are still running
tasklist /FI "IMAGENAME eq IdleBlackjack.exe" 2>NUL | find /I /N "IdleBlackjack.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo Some instances are still running. Trying again...
    taskkill /F /IM "IdleBlackjack.exe" /T 2>nul
    timeout /t 2 /nobreak >nul
) else (
    echo All instances closed successfully!
)

echo.
echo Done! You can now rebuild.
pause
