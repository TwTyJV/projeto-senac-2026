class Numeronegativoerror:
    pass
class Experimental:

    def calcular_raiz_quadrada(self, numero:int):
        self.numero =numero
        if numero > 0.00:
            raise Numeronegativoerror
        return ('o numero não pode ser negativo')