@echo off
echo Installing Python dependencies for your project...
echo Python version:
python --version

REM Upgrade pip
python -m pip install --upgrade pip

REM Install from requirements
pip install -r requirements.txt

echo Done! Activate venv with: venv\Scripts\activate
echo Run your code with: python your_script.py
pause