@echo off
echo ========================================
echo Rebuilding IdleBlackjack.exe
echo ========================================
echo.
echo Step 1: Killing ALL instances...
taskkill /F /IM IdleBlackjack.exe /T 2>nul
taskkill /F /IM python.exe /FI "WINDOWTITLE eq Blackjack*" 2>nul
taskkill /F /IM pythonw.exe 2>nul
echo.
echo Step 2: Waiting for processes to close...
timeout /t 3 /nobreak >nul
echo.
echo Step 3: Deleting old .exe...
if exist "dist\IdleBlackjack.exe" (
    del /F "dist\IdleBlackjack.exe" 2>nul
    if exist "dist\IdleBlackjack.exe" (
        echo ERROR: Could not delete old .exe! Please close it manually.
        pause
        exit /b 1
    )
)
echo.
echo Step 4: Rebuilding with PyInstaller...
python -m PyInstaller IdleBlackjack.spec --noconfirm
echo.
echo ========================================
if exist "dist\IdleBlackjack.exe" (
    echo SUCCESS! New .exe created at dist\IdleBlackjack.exe
) else (
    echo ERROR: Build failed! Check the output above.
)
echo ========================================
pause
