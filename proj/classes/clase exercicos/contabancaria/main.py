from conta import ContaBancaria

if __name__ == '__main__':

    contabancaria = ContaBancaria('joão')
    contabancaria2 = ContaBancaria('jorge')

    contabancaria.depositar(20.0)
    contabancaria.transferir(contabancaria2, 10.0)

    print(contabancaria.saldo)
    print(contabancaria2.saldo)