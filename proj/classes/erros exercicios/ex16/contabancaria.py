class SaldoInsuficienteError(Exception):
    def __init__(self, faltante):
        super().__init__(f"Saldo insuficiente. Faltam R$ {faltante:.2f}.")
        self.faltante = faltante


class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def sacar(self, valor: int):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")

        if valor > self.saldo:
            faltante = valor - self.saldo
            raise SaldoInsuficienteError(faltante)

        self.saldo -= valor
        return self.saldo

    def consultar_saldo(self):
        return self.saldo