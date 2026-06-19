from area import analisar_dimensoes_casa

if __name__ == '__main__':
    try:
        analisar_dimensoes_casa('proj/classes/arquivos_ex/arquivo_teste/planta_casa.txt')

    except ValueError:
        print('está vaizio')

    
