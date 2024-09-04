import subprocess  # Import the subprocess module to allow running system commands from Python.
import yaml  # Import the yaml module to read and manipulate YAML configuration files.

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

def list_models():
    """
    Function to list the available models using the 'ollama list' command.
    Returns a list of model names.
    """
    print("Listing available models...")  # Display a message indicating that models are being listed.
    try:
        # Run the command 'ollama list' to retrieve the list of models
        result = subprocess.run(
            ['C:/Users/blc/AppData/Local/Programs/Ollama/ollama.exe', 'list'],  # Specify the command and arguments to run
            capture_output=True,  # Capture the output of the command
            text=True,  # Interpret the output as text (string) instead of bytes
            check=True  # Raise an error if the command returns a non-zero exit code
        )
        # Process the command's output: remove any leading/trailing whitespace and split into lines
        models = result.stdout.strip().splitlines()
        
        # Filter out any lines that are not model names (e.g., header, error messages)
        model_names = [line.split()[0]  # Extract the first word (model name) from each line
                       for line in models  # Iterate over each line in the output
                       if len(line.split()) > 1 and line.split()[0] not in ['NAME', 'failed']]  
                       # Check that the line has more than one word and doesn't start with 'NAME' or 'failed'

        return model_names  # Return the list of model names
    except subprocess.CalledProcessError as e:
        # If the command fails, catch the exception and print an error message
        print(f"Error listing models: {e}")
        return []  # Return an empty list if an error occurs


def select_model(models):
    """
    Function to display the models and allow the user to select one.
    Returns the name of the selected model.
    """
    if not models:
        # Raise an error if no models are available
        raise RuntimeError("No models available.")

    print("Available models:")  # Display a message listing the available models
    for idx, model in enumerate(models, start=1):
        # Print each model with its corresponding number
        print(f"{idx}. {model}")

    try:
        # Prompt the user to select a model by entering its number
        choice = int(input("Enter the number of the model you want to run: ")) - 1
        if choice < 0 or choice >= len(models):
            # Raise an error if the selection is out of bounds
            raise ValueError("Invalid selection.")
        return models[choice]  # Return the selected model name
    except ValueError:
        # Handle invalid input and prompt the user to try again
        print("Invalid input. Please enter a valid number.")
        return select_model(models)  # Retry model selection if the input is invalid

def run_ollama():
    """
    Main function that lists models, allows selection, and runs Ollama with the selected model.
    """
    models = list_models()  # List available models
    model_name = select_model(models)  # Allow the user to select a model
    
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
