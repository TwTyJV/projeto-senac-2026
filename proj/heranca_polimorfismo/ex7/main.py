from proj.heranca_polimorfismo.ex7.violao import Violão
from proj.heranca_polimorfismo.ex7.flauta import Flauta
from proj.heranca_polimorfismo.ex7.bateria import Bateria

if __name__ == '__main__':

    violao = Violão ()
    flauta = Flauta()
    bateria = Bateria()

    for i in range (3):
        print(violao.tocar())
        print(flauta.tocar())
        print(bateria.tocar())
        
