class ContaBancaria:

    titular:str  
    saldo:float

    def __init__(self, titular:str):
        self.titular = titular
        self.saldo = 0.0


    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.saldo += valor

    def sacar(self, valor: float) -> bool:
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False