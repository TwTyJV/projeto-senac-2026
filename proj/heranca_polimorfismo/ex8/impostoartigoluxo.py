from proj.heranca_polimorfismo.ex8.calculadordeimposto import Calculadordeimposto

class Impostoartigoluxo(Calculadordeimposto):

    def calcular(self, valor:float):
        return valor * 0.20