class Saldoinsuficienteerror(Exception):
    def __init__(self, mensagem="Saldo insuficiente para realizar o saque."):
        super().__init__(mensagem)

class Contabancaria:
    def __init__(self, titular:str, saldo:float):
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("O valor do saque deve ser numérico.")

        if valor > self.saldo:
            raise Saldoinsuficienteerror()

        self.saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado. Saldo atual: R$ {self.saldo:.2f}")


def processar_lote_saques(conta_objeto:str, lista_de_valores:list):
    saques_nao_executados = []

    for indice, valor in enumerate(lista_de_valores):
        try:
            conta_objeto.sacar(valor)

        except TypeError:
            print(f"Aviso: '{valor}' é um valor inválido. Saque ignorado.")
            continue

        except Saldoinsuficienteerror as erro:
            print(f"Erro: {erro}")

            # Guarda todos os saques que não serão mais processados
            saques_nao_executados = lista_de_valores[indice:]
            break

    return saques_nao_executados
