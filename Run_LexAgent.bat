@echo off
TITLE LexAgent Legal Tech Launcher
cd /d "%~dp0"

IF EXIST "env\Scripts\activate.bat" (
    call env\Scripts\activate.bat
) ELSE IF EXIST "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) ELSE (
    echo Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    pip install -r requirements.txt
)

echo ======================================================================
echo  ⚖️ Launching LexAgent Legal Tech Web App...
echo ======================================================================
streamlit run app.py
pause
