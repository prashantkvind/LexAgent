#!/usr/bin/env bash
# 🚀 LexAgent Launcher for macOS & Linux
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

if [ -d "env" ]; then
    source env/bin/activate
elif [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "Virtual environment not found. Running setup.sh first..."
    ./setup.sh
    source env/bin/activate
fi

echo "======================================================================"
echo " ⚖️ Launching LexAgent Legal Tech Web App..."
echo "======================================================================"
streamlit run app.py
