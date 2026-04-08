@echo off
setlocal

:: Read version from package.json
for /f "tokens=2 delims=:," %%a in ('findstr "version" package.json') do (
    set RAW=%%a
)
set VERSION=%RAW: =%
set VERSION=%VERSION:"=%
echo Building Calamari Union v%VERSION%

:: Activate venv if it exists
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

:: Install dependencies
pip install -q pygame-ce pyinstaller

:: Clean previous build
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

:: Build with PyInstaller — single exe, no console
python -m PyInstaller ^
    --onefile ^
    --noconsole ^
    --name "CalamarUnion-v%VERSION%" ^
    --clean ^
    main.py

:: Copy to game folder
if exist "dist\CalamarUnion-v%VERSION%.exe" (
    copy "dist\CalamarUnion-v%VERSION%.exe" . >nul
    echo.
    echo Build complete: CalamarUnion-v%VERSION%.exe
) else (
    echo.
    echo Build failed!
    exit /b 1
)

endlocal
