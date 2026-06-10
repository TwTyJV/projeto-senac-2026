from impostoartigoluxo import Impostoartigoluxo
from calculadordeimposto import Calculadordeimposto

if __name__ == '__main__':

    impostoartigoluxo = Impostoartigoluxo()
    calculadordeimposto = Calculadordeimposto()

    valor=1000
    print(impostoartigoluxo.calcular(valor))
    print(calculadordeimposto.calcular(valor))
    