@echo off
echo "Starting batch script..."

REM Navigate to your project directory
cd /d "D:\OneDrive - InMotion - Consulting\AI Projects\ollama-python-runner"
IF %ERRORLEVEL% NEQ 0 (
    echo "Failed to navigate to project directory."
    exit /b
)

REM Check if the virtual environment exists
IF NOT EXIST venv (
    echo "Virtual environment not found. Please set it up first."
    exit /b
)

REM Activate the virtual environment
call venv\Scripts\activate
IF %ERRORLEVEL% NEQ 0 (
    echo "Failed to activate the virtual environment."
    exit /b
)

REM Wait for 2 seconds to ensure environment is fully loaded
timeout /t 2 /nobreak > NUL

REM Verify Python version
python --version

REM Run the Python script
python src\main.py
IF %ERRORLEVEL% NEQ 0 (
    echo "Python script execution failed."
    exit /b
)

echo "Batch script completed."
pause
