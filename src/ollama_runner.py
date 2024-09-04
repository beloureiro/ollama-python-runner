import subprocess  # Import the subprocess module to allow running system commands from Python.
import yaml  # Import the yaml module to read and manipulate YAML configuration files.
import time  # Import the time module to allow adding delays.
import psutil  # Importar psutil para verificar processos em execução

def load_config():
    """
    Function to load the configuration from the config.yaml file.
    """
    print("Loading configuration...")  # Display a message indicating that the configuration is being loaded.
    
    # Open the config.yaml file for reading
    with open("config/config.yaml", "r") as file:
        # Load the content of the YAML file into a Python dictionary
        config = yaml.safe_load(file)
    
    print("Configuration loaded.")  # Indicate that the configuration has been successfully loaded.
    return config  # Return the dictionary with the loaded configuration.

def is_ollama_running():
    """
    Function to check if the Ollama process is running.
    """
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'ollama.exe':
            return True
    return False

def is_ollama_ready():
    """
    Function to check if the Ollama executable is ready to respond.
    """
    print("Checking if Ollama is ready...")  # Debug message
    if not is_ollama_running():
        print("Ollama is not running. Please start the Ollama application.")  # Mensagem de erro
        return False

    for attempt in range(5):  # Try up to 5 times before giving up
        try:
            print(f"Attempt {attempt + 1} to check Ollama status...")  # Debug message
            result = subprocess.run(
                ['C:/Users/blc/AppData/Local/Programs/Ollama/ollama.exe', 'list'],
                capture_output=True, text=True, check=True,
                timeout=10  # Timeout de 10 segundos
            )
            if result.returncode == 0:
                print("Ollama is ready.")  # Debug message
                return True  # Ollama is ready
        except subprocess.CalledProcessError as e:
            print(f"Ollama not ready, retrying... ({e})")  # Debug message
            time.sleep(2)  # Wait for 2 seconds before retrying
        except subprocess.TimeoutExpired:
            print("Ollama did not respond in time, retrying...")  # Debug message
            time.sleep(2)  # Wait for 2 seconds before retrying

    print("Ollama is not ready after 5 attempts.")  # Debug message
    return False  # Ollama is not ready

def list_models():
    """
    Function to list the available models using the 'ollama list' command.
    Returns a list of model names.
    """
    if not is_ollama_ready():
        print("Ollama is not ready. Please start the Ollama application and try again.")
        return []  # Retorna uma lista vazia se o Ollama não estiver pronto

    print("Listing available models...")  # Debug message
    try:
        result = subprocess.run(
            ['C:/Users/blc/AppData/Local/Programs/Ollama/ollama.exe', 'list'],
            capture_output=True,
            text=True,
            check=True
        )
        models = result.stdout.strip().splitlines()
        model_names = [line.split()[0] for line in models if len(line.split()) > 1 and line.split()[0] not in ['NAME', 'failed']]
        
        print(f"Models found: {model_names}")  # Debug message
        return model_names  # Return the list of model names
    except subprocess.CalledProcessError as e:
        print(f"Error listing models: {e}")
        return []  # Return an empty list if an error occurs

def select_model(models):
    """
    Function to display the models and allow the user to select one.
    Returns the name of the selected model or None if the user chooses to exit.
    """
    if not models:
        # Raise an error if no models are available
        raise RuntimeError("No models available.")

    while True:
        print("Available models:")  # Display a message listing the available models
        for idx, model in enumerate(models, start=1):
            # Print each model with its corresponding number
            print(f"{idx}. {model}")

        choice = input("Enter the number of the model you want to run or type 'exit' to quit: ").strip().lower()

        if choice in ['exit', 'q']:  # Check if the user wants to exit
            print("Exiting the program.")
            return None
        
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(models):
                return models[choice]  # Return the selected model name
        
        print("Invalid input. Please enter a valid number or 'exit' to quit.")  # Handle invalid input and prompt the user to try again

def run_ollama():
    """
    Main function that lists models, allows selection, and runs Ollama with the selected model.
    """
    print("Starting the Ollama runner...")  # Debug message
    models = list_models()  # List available models
    if not models:
        return  # Exit if no models are available or Ollama is not ready

    model_name = select_model(models)  # Allow the user to select a model
    
    if model_name is None:
        return  # Exit if the user chose to quit
    
    print(f"Starting Ollama with model: {model_name}...")  # Display a message indicating which model is being started
    config = load_config()  # Load the configuration file

    try:
        # Run the Ollama command with the selected model
        result = subprocess.run(
            ['C:/Users/blc/AppData/Local/Programs/Ollama/ollama.exe', 'run', model_name]
        )
        
        # Check if the command was successful
        if result.returncode != 0:
            raise RuntimeError(f"Ollama execution failed with return code {result.returncode}")

        print("Ollama ran successfully.")  # Indicate that Ollama ran successfully
    
    except subprocess.TimeoutExpired:
        # Handle the case where the command times out
        raise RuntimeError("Ollama execution timed out.")
