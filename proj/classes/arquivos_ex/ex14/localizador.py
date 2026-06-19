def inventariar_moveis(nome_arquivo:str):
    
    inventario = {}
    
    with open(nome_arquivo, "r",) as arquivo:
        for linha in arquivo.readlines(): 
            for linha in enumerate(linha):
                linha = linha.strip('\n')