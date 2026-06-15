from autenticador import Autenticador, ContaBloqueadaError

if __name__ == '__main__':

    autenticador = Autenticador()

    try:
        autenticador.fazer_login(1111)
        autenticador.fazer_login(2222)
        autenticador.fazer_login(3333)
    except ValueError:
        print("Senha incorreta")
    except ContaBloqueadaError:
        print("Cartão bloqueado")