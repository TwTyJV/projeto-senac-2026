from experimental import Experimental, Numeronegativoerror

if __name__ == '__main__':

    experimental = Experimental()

    try:
        print(experimental.calcular_raiz_quadrada(-2))
    except Numeronegativoerror: 
        print('O numero não pode ser negativo')