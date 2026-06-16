class Erros:

    def verificar_sinal(self, numero:int):
        if numero < 0:
            raise ValueError('o número não pode ser negativo')