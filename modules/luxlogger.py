import time
from datetime import datetime
from modules.bht1750 import BH1750
from modules.sdcard import SdCard


class LuxLogger:
    
    # Inicializa o logger
    def __init__(self, storage_path='/media/caninos/DADOS_SD', log_filename='lux_log.txt'):
        self.sd_card = SdCard(storage_path)
        self.sensor = BH1750()
        self.log_filename = log_filename
        
        # Configura SD card
        if not self.sd_card.setup():
            raise RuntimeError("Erro ao configurar SD card")
        
        print("INFO: Sistema configurado com sucesso")
    
    # Faz uma leitura e salva no arquivo
    def log(self, notes=""):
        lux = self.sensor.read_lux()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = f"{timestamp}, {lux:.2f} lux {f'[{notes}]' if notes else ''}"
        
        if self.sd_card.append_file(self.log_filename, data):
            print(f"LOG: {data}")
            return lux
        
        print("ERRO: Falha ao salvar dados")
        return None
    
    # Faz leituras contínuas indefinidamente
    def log_continuous(self, interval=1):
        """Faz leituras contínuas indefinidamente"""
        print(f"INFO: Iniciando logging contínuo com intervalo de {interval}s")
        print("INFO: Pressione Ctrl+C para parar")
        
        count = 0
        try:
            while True:
                time.sleep(interval)
                self.log()
        except KeyboardInterrupt:
            print(f"\nINFO: Logging parado após {count} leituras")
            print("INFO: Sistema parado pelo usuário")
    
    # Fecha as conexões
    def close(self):
        """Fecha conexões"""
        self.sensor.close()
        print("INFO: Sistema fechado")
