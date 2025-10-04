from modules.luxlogger import LuxLogger

def main():
    try:
        # Cria o logger
        logger = LuxLogger()
        
        # Faz uma leitura de teste
        logger.log("Teste inicial")
        
        # Inicia logging contínuo (roda indefinidamente)
        logger.log_continuous(interval=2)
        
    except Exception as e:
        print(f"ERRO: {e}")
    finally:
        # Garante que o sistema seja fechado
        try:
            logger.close()
        except:
            pass
    
if __name__ == "__main__":
    main()
