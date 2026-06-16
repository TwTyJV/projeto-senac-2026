def ler_poema():
    try:
        with open('poema.txt', 'r') as arquivo:
            arquivo.read(ler_poema)

    except FileNotFoundError:
        return('arquivo fisico não localizado')