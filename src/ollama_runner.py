import subprocess  # Importa o módulo subprocess, que permite executar comandos do sistema operacional a partir do Python.
import yaml  # Importa o módulo yaml, que é usado para ler e manipular arquivos de configuração no formato YAML.

def load_config():
    """
    Função que carrega a configuração a partir do arquivo config.yaml.
    """
    print("Carregando configuração...")  # Exibe uma mensagem informando que a configuração está sendo carregada.
    
    # Abre o arquivo config.yaml para leitura
    with open("config/config.yaml", "r") as file:
        # Carrega o conteúdo do arquivo YAML em um dicionário Python
        config = yaml.safe_load(file)
    
    print("Configuração carregada.")  # Informa que a configuração foi carregada com sucesso.
    return config  # Retorna o dicionário com as configurações carregadas.

def run_ollama(model_name):
    """
    Função que executa o Ollama com o modelo especificado.
    Recebe como parâmetro o nome do modelo (model_name) e retorna a saída da execução.
    """
    print(f"Iniciando o Ollama com o modelo: {model_name}...")  # Exibe uma mensagem informando qual modelo será executado.
    
    config = load_config()  # Carrega a configuração usando a função load_config().

    try:
        # Executa o comando para rodar o Ollama. 
        # Aqui, o subprocess.run é usado para chamar o executável do Ollama com o modelo fornecido.
        result = subprocess.run(
            ['C:/Users/blc/AppData/Local/Programs/Ollama/ollama.exe', 'run', model_name]
            # A lista ['C:/Users/blc/AppData/Local/Programs/Ollama/ollama.exe', 'run', model_name] especifica:
            # 1. O caminho completo para o executável do Ollama.
            # 2. O comando 'run' que instrui o Ollama a rodar o modelo.
            # 3. O nome do modelo (model_name) que foi passado para a função.
        )
        
        # Verifica se o comando foi executado com sucesso
        if result.returncode != 0:  # result.returncode guarda o código de retorno do comando (0 indica sucesso).
            raise RuntimeError(f"Ollama execution failed with return code {result.returncode}")
            # Se o código de retorno for diferente de 0, levanta um erro informando que a execução falhou.

        print("Ollama rodou com sucesso.")  # Se tudo correu bem, informa que o Ollama rodou com sucesso.
    
    except subprocess.TimeoutExpired:
        # Caso o comando demore mais do que o tempo limite (timeout), um erro será levantado.
        raise RuntimeError("Ollama execution timed out.")
