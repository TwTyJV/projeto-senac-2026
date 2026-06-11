from segurança import Segurança

if __name__ == '__main__':

    segurança = Segurança ()
    lista = ['mexico']

    try:
        print(segurança.obter_elemento(lista,4))
    except IndexError:
        print(segurança.obter_elemento('não existe esse lugar'))