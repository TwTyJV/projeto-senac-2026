from combinadas import Combinadas

if __name__ == '__main__':

    combinadas = Combinadas()

    try:
        print(combinadas.validar_usuario('oi'))
    except ValueError:
        print('Não pode ter menos de 3 caracteias')