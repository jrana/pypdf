@echo off
echo ========================================
echo Building PyPDF Windows Executable
echo ========================================
echo.

REM Check if PyInstaller is installed
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo Installing PyInstaller...
    pip install pyinstaller
    echo.
)

echo Building executable...
echo.

pyinstaller pypdf.spec --clean

echo.
if exist "dist\PyPDF.exe" (
    echo ========================================
    echo Build successful!
    echo Executable location: dist\PyPDF.exe
    echo ========================================
) else (
    echo ========================================
    echo Build may have failed. Check output above.
    echo ========================================
)

pause

