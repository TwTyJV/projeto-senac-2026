from calculadordeimposto import Calculadordeimposto

class Impostoartigoluxo(Calculadordeimposto):

    def calcular(self, valor:float):
        return valor * 0.20