def contar_linhas_arquivo(nome_arquivo:str):
        contagem = 0
        with open(nome_arquivo) as arquivo:
            for linha in arquivo.readlines():
                if  linha.endswith('\n') or linha.startswith('\n'):
                    contagem+=1

        return contagem