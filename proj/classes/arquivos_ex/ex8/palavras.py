def buscar_palavra_no_texto(palavra_alvo:str):
    with open('documento.txt', 'r') as arquivo:
        for index, linha in enumerate(arquivo.readlines()):
            if linha.find(palavra_alvo):
                print(f"Linha {index}: {linha.strip()}")