from contabancaria import ContaBancaria, SaldoInsuficienteError

if __name__ == '__main__':

    conta = ContaBancaria(0)

    try:
        valor_saque = 150

        print("Saldo atual:", conta.consultar_saldo())
        print("Tentando sacar:", valor_saque)

        conta.sacar(valor_saque)

    except SaldoInsuficienteError as e:
        print("Seu saldo é insuficiente.")
        print(e)
        print("Faltam:", e.faltante)