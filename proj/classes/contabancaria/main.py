from contabancaria import ContaBancaria

if __name__ == '__main__':

    conta = ContaBancaria("joão")
    conta.depositar (100)

    assert conta.saldo == 100

    assert conta.sacar(2) is True