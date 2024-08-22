from ollama_runner import run_ollama  # Importa a função run_ollama do arquivo ollama_runner.py

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente (não importado como um módulo)
    model_name = "llama3.1:8b"  # Define o nome do modelo a ser executado. Pode ser substituído pelo nome de qualquer outro modelo disponível.
    
    try:
        # Tenta executar a função run_ollama usando o modelo especificado
        output = run_ollama(model_name)
        
        # Se a execução foi bem-sucedida, imprime a mensagem e a saída do modelo
        print("Modelo rodado com sucesso:")
        print(output)
    
    except Exception as e:
        # Se houver qualquer erro durante a execução, captura a exceção e imprime uma mensagem de erro
        print("Erro ao rodar o modelo:", e)
