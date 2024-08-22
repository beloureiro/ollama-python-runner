@echo off
cd /d "D:\OneDrive - InMotion - Consulting\AI Projects\ollama-python-runner"  # Navigate to your project directory
call venv\Scripts\activate  # Activate the virtual environment
python src\main.py  # Run the Python script
pause  # Keeps the command prompt open after the script runs
