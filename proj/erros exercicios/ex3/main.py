from customizada import Entrada_errada, ErroDeEntradaInvalida

if __name__ == '__main__':


    try:
        print(Entrada_errada('param'))
    except ErroDeEntradaInvalida:
        print('valor invalido, o valor deviria ser param')
    