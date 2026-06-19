def gravar_diario(mensagem:str):
    with open('diaria.txt', 'w') as arquivo:
        arquivo.write(mensagem)