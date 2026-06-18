def limpar_arquivo(origem:str, destino:str):
        lista = []
        with open(origem,  'r') as arquivo:
            for linha in arquivo.readlines():
                linha.strip()
                lista.append(linha)
            
        
        with open(destino, 'w') as arq_dest:
            for linha in lista:
                arq_dest.write(linha)

        
