from periphery import I2C
import time
import os

class BH1750:
    # Inicializa o sensor BH1750
    def __init__(self):
        self.i2c = None
        self.addr = None
        
        # Tenta encontrar e conectar ao sensor
        for bus in ["/dev/i2c-0", "/dev/i2c-1", "/dev/i2c-2"]:
            if not os.path.exists(bus):
                continue
                
            for addr in [0x23, 0x5C]:
                try:
                    self.i2c = I2C(bus)
                    self.addr = addr
                    
                    # Testa conexão
                    self.i2c.transfer(addr, [I2C.Message([0x01])])
                    time.sleep(0.01)
                    
                    # Define modo contínuo
                    self.i2c.transfer(addr, [I2C.Message([0x10])])
                    time.sleep(0.12)
                    
                    print(f"INFO: Sensor BH1750 encontrado em {bus}, endereço 0x{addr:02x}")
                    return
                    
                except:
                    if self.i2c:
                        self.i2c.close()
                    continue
        
        raise RuntimeError("ERRO: Sensor BH1750 não encontrado!")

    # Lê o valor de luminosidade
    def read_lux(self):
        read_msg = [I2C.Message([0x00] * 2, read=True)]
        self.i2c.transfer(self.addr, read_msg)
        
        data = read_msg[0].data
        lux_raw = (data[0] << 8) | data[1]
        return lux_raw / 1.2

    # Fecha a conexão I2C
    def close(self):
        if self.i2c:
            self.i2c.close()
            print("INFO: Sensor BH1750 desconectado")
