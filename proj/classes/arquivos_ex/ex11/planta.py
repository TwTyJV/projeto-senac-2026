def mapear_paredes_planta(nome_arquivo:str):

    
    try:
        lista = []
        with open(nome_arquivo, "r") as arquivo:
                for indice_linha, linha in enumerate(arquivo.readlines()):
                    for indice_coluna, caractere in enumerate(linha):
                        if caractere == "=":
                            lista.append((indice_linha, indice_coluna))
                return lista
        
    except FileNotFoundError:
        ('Arquivo não encontrado')