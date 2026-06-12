from bloco import Bloco

if __name__ == '__main__':

    bloco = Bloco()
    
    try:
        print(bloco.simular_banco_de_dados('sql'))
    except Exception:
        ("Deu erro")
    finally:
        print("Conexão encerrada.")