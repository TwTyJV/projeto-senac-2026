def somar_valores_arquivo():
    soma = 0.0

    try:
        with open("valores.txt", "r") as arquivo:
            for numero_linha, linha in enumerate(arquivo, start=1):
                try:
                    valor = float(linha.strip())
                    soma += valor
                except ValueError:
                    print(f"Erro na linha {numero_linha}: '{linha.strip()}' não é um número válido.")

        print(f"Soma total dos valores: {soma}")

    except FileNotFoundError:
        print("Erro o arquivo não foi encontrado.")