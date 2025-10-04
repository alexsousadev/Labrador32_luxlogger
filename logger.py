import time
from datetime import datetime
from modules.bht1750 import BH1750
from modules.sdcard import SdCard

def log_reading(sd_card, sensor, log_filename, notes=""):
    """Faz uma leitura e salva no arquivo"""
    lux = sensor.read_lux()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = f"{timestamp}, {lux:.2f} lux {f'[{notes}]' if notes else ''}"
    
    if sd_card.append_file(log_filename, data):
        print(f"LOG: {data}")
        return lux
    
    print("ERRO: Falha ao salvar dados")
    return None


def log_continuous(sd_card, sensor, log_filename, interval=1):
    """Faz leituras contínuas indefinidamente"""
    print(f"INFO: Iniciando logging contínuo com intervalo de {interval}s")
    print("INFO: Pressione Ctrl+C para parar")
    
    count = 0
    try:
        while True:
            time.sleep(interval)
            log_reading(sd_card, sensor, log_filename)
            count += 1
    except KeyboardInterrupt:
        print(f"\nINFO: Logging parado após {count} leituras")
        print("INFO: Sistema parado pelo usuário")


def main():
    storage_path = '/media/caninos/DADOS_SD'
    log_filename = 'lux_log.txt'
    
    try:
        # Inicializa componentes
        sd_card = SdCard(storage_path)
        sensor = BH1750()
        
        # Configura SD card
        if not sd_card.setup():
            raise RuntimeError("Erro ao configurar SD card")
        
        print("INFO: Sistema configurado com sucesso")
        
        # Faz uma leitura de teste
        log_reading(sd_card, sensor, log_filename, "Teste inicial")
        
        # Inicia logging contínuo (roda indefinidamente)
        log_continuous(sd_card, sensor, log_filename, interval=2)
        
    except Exception as e:
        print(f"ERRO: {e}")
    finally:
        # Garante que o sistema seja fechado
        try:
            sensor.close()
            print("INFO: Sistema fechado")
        except:
            pass
    
if __name__ == "__main__":
    main()
