# Ollama Python Runner

This project enables the execution of language models from Ollama using Python. It is designed to facilitate the use of large language models like `llama3.1:8b` directly from Python scripts, with support for custom configurations and GPU usage. The project now includes a feature to list available models and allow the user to select a model via an interactive loop before running the selected model.

## Project Structure

- **src/**: Contains the main code of the project.
  - **ollama_runner.py**: Script that lists available models, allows model selection, and runs the selected Ollama model.
  - **main.py**: Entry script that initiates the model selection and execution.
- **tests/**: Contains tests for the project.
- **config/**: Contains configuration files.
  - **config.yaml**: Configuration file that defines the model path, GPU usage, and logging settings.
- **logs/**: Directory where execution logs are stored.
- **venv/**: Python virtual environment to isolate dependencies.

## Requirements

- Python 3.12 or higher
- Ollama installed and configured
- Dependencies listed in `requirements.txt`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your_username/ollama-python-runner.git
   cd ollama-python-runner
   ```

2. Create and activate the virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the `config/config.yaml` file to adjust the model and logging settings as needed.

## Usage

To run a model with Ollama, execute the main script:

```bash
python src/main.py
```

This will list the available models, prompt you to select a model by entering its corresponding number, and then run the selected model with the provided configurations.

## Customization

- **Model Configuration**: Adjust the model path and other options in the `config/config.yaml` file.
- **GPU Usage**: Enable or disable GPU usage in the same configuration file.
- **Log Levels**: Change the log level to get more or less detail during execution.

## Contribution

Contributions are welcome! To contribute, fork the repository, create a branch for your feature or fix, and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
