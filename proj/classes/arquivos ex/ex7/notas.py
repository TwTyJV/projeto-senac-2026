def calcular_medias_alunos():
    try:
        nomes_e_medias = [{}]
        caminho_arquivo = 'proj/classes/arquivo ex/arquivo ex/notas.txt'
        with open(caminho_arquivo) as arquivo_entrada:
            for linhas in arquivo_entrada.readlines():
                dados = linhas.split(',')
                nome = dados[0], 
                nota1 = float(dados[1])
                nota2 = float(dados[2])
                media = (nota1 + nota2) / 2

                nomes_e_medias.append({'nome' :nome,'media':media})
    except FileNotFoundError:
        print('Arquivo não encontrado')
        return
    finally:
        if not nomes_e_medias:
            return None
        
        with open('medias_finais.txt', 'w') as arquivo:
            for objeto in nomes_e_medias:
                arquivo.write(f"{objeto.get('nome')}, {objeto.get('media')}")



