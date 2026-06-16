from idadeinvalidaerror import IdadeInvalidaError, cadastrar_eleitor

if __name__ == "__main__":

    try:
        cadastrar_eleitor(10) 
    except IdadeInvalidaError as e:
        print(f"Erro capturado: {e}")