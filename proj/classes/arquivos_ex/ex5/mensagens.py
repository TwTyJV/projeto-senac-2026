def filtrar_erros():

    lista_erros = []
    with open("proj/classes/arquivos ex/arquivos_teste/sistema.log", "r") as arquivo_log:
        for linha in arquivo_log.readlines():
            if linha.startswith("ERROR"):
                lista_erros.append(linha)
        
    with open("alertas_criticos.txt", "w") as arquivo_alertas:
        for linha in lista_erros:
            arquivo_alertas.write(linha + '\n')
    