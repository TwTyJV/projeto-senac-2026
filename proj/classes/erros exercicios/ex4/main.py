from erros import Erros

if __name__ == '__main__':

    erros = Erros ()

    try:
        print(erros.verificar_sinal(-2))
    except ValueError:
        print('O numero não pode ser menor que zero')
