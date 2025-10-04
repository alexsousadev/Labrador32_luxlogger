import time
from datetime import datetime
from modules.sdcard import SdCard

def main():
    print("Iniciando sistema de logging...")
    
    # Criar instância do SdCard
    sd_card = SdCard('/media/caninos/DADOS_SD')
    
    # Configurar armazenamento
    if not sd_card.setup():
        print("ERRO: Não foi possível configurar o armazenamento")
        return
    
    print("Armazenamento configurado!")
    
    # Loop de logging
    for i in range(10):
        # Criar dados para gravar
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")   
        log_filename = "data_logger.txt"
        data = f"{timestamp}, Contador: {i}"
        print(f"Gravando: {data}")
        
        # Gravar dados no arquivo
        if sd_card.append_file(log_filename, data):
            print(f"✓ Dados gravados com sucesso (linha {i+1})")
        else:
            print(f"✗ Erro ao gravar dados (linha {i+1})")
        
        time.sleep(1)
    
    print("Logging concluído!")

if __name__ == "__main__":
    main()
