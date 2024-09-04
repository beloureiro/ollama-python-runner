# Import the run_ollama function from the ollama_runner.py file
from ollama_runner import run_ollama  

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    try:
        # Attempt to execute the Ollama with the model selection logic
        run_ollama()
    except Exception as e:
        # If any error occurs during execution, capture the exception and print an error message
        print("Error running the model:", e)
