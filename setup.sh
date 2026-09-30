#!/usr/bin/env bash
set -e

echo "======================================================================"
echo " ⚙️ LexAgent Environment Setup Script"
echo "======================================================================"

# Create virtual environment if not existing
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment in venv/..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing/updating dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "======================================================================"
echo " ✅ Setup Complete!"
echo " To run CLI mode:         python3 main.py"
echo " To run Streamlit UI:     streamlit run app.py"
echo " To run Pytest suite:     pytest tests/ -v"
echo "======================================================================"
