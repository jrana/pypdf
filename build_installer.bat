@echo off
echo ============================================
echo PyPDF Build Script
echo ============================================
echo.

:: Check for Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

:: Check for PyInstaller
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo Installing PyInstaller...
    pip install pyinstaller
)

echo.
echo [Step 1/3] Building Windows Executable...
echo ============================================
pyinstaller --name "PyPDF" --windowed --onefile --icon "img/pypdf.ico" --add-data "img;img" --add-data "help.html;." pypdf.py --noconfirm

if errorlevel 1 (
    echo ERROR: PyInstaller build failed
    pause
    exit /b 1
)

echo.
echo [Step 2/3] Executable created successfully!
echo Location: dist\PyPDF.exe
echo.

:: Check for Inno Setup
set ISCC_PATH=
if exist "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" (
    set "ISCC_PATH=C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
) else if exist "C:\Program Files\Inno Setup 6\ISCC.exe" (
    set "ISCC_PATH=C:\Program Files\Inno Setup 6\ISCC.exe"
)

if "%ISCC_PATH%"=="" (
    echo.
    echo [Step 3/3] Inno Setup not found!
    echo ============================================
    echo To build the Windows installer, please:
    echo 1. Download Inno Setup from: https://jrsoftware.org/isdl.php
    echo 2. Install Inno Setup 6
    echo 3. Run this script again, OR
    echo 4. Open installer.iss in Inno Setup and click Build
    echo.
    echo The executable is ready at: dist\PyPDF.exe
    pause
    exit /b 0
)

echo [Step 3/3] Building Windows Installer...
echo ============================================

:: Create installer output directory
if not exist "installer" mkdir installer

:: Build the installer
"%ISCC_PATH%" installer.iss

if errorlevel 1 (
    echo ERROR: Installer build failed
    pause
    exit /b 1
)

echo.
echo ============================================
echo BUILD COMPLETE!
echo ============================================
echo.
echo Executable: dist\PyPDF.exe
echo Installer:  installer\PyPDF_Setup_2.2.exe
echo.
pause

