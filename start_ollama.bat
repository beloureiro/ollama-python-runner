@echo off
REM Navigate to your project directory
cd /d "D:\OneDrive - InMotion - Consulting\AI Projects\ollama-python-runner"

REM Check if the virtual environment exists
IF NOT EXIST venv (
    echo Virtual environment not found. Please set it up first.
    exit /b
)

REM Activate the virtual environment
call venv\Scripts\activate

REM Run the Python script
python src\main.py

REM Keeps the command prompt open after the script runs
pause
