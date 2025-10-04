import os

ENCODING = 'utf-8'

class SdCard:

    # Inicializa o gerenciador do cartão SD
    def __init__(self, storage_path, encoding=ENCODING):
        self.storage_path = storage_path
        self.encoding = encoding
    
    # Configura o diretório de armazenamento
    def setup(self):
        try:
            os.makedirs(self.storage_path, exist_ok=True)
            print(f"INFO: Diretório '{self.storage_path}' configurado com sucesso")
            return True
        except Exception as e:
            print(f"ERRO: {e}")
            return False
    
    # Escreve conteúdo em um arquivo
    def write_file(self, filename, content):
        try:
            full_path = os.path.join(self.storage_path, filename)
            os.makedirs(self.storage_path, exist_ok=True)
            
            with open(full_path, 'w', encoding=self.encoding) as f:
                f.write(str(content))
            return True
        except Exception as e:
            print(f"ERRO: Falha ao escrever arquivo: {e}")
            return False
    
    # Adiciona conteúdo a um arquivo
    def append_file(self, filename, content):
        try:
            full_path = os.path.join(self.storage_path, filename)
            os.makedirs(self.storage_path, exist_ok=True)
            
            with open(full_path, 'a', encoding=self.encoding) as f:
                f.write(f"{content}\n")
            return True
        except Exception as e:
            print(f"ERRO: Falha ao adicionar ao arquivo: {e}")
            return False


