def analisar_dimensoes_casa(nome_arquivo:str):

    linha = []
    try:
        with open(nome_arquivo, "r") as arquivo:
            perimetro = 0
            area_util = 0
        
            for linha in arquivo.readlines():
                  for linha, caracter in arquivo.readlines(linha):
                        if caracter == '=':
                            perimetro+= linha.count('=')
                            area_util += linha.count('')

                         
            
    except ValueError:
        return ('Está vazio')
            

                              
                            