from proj.heranca_polimorfismo.ex10.heroi import Heroi
from proj.heranca_polimorfismo.ex10.guerreiro import Guerreiro
from proj.heranca_polimorfismo.ex10.mago import Mago

if __name__ == '__main__':

    heroi = Heroi("Cr7", 100)
    mago = Mago("Neymar", 80, 30)
    guerreiro = Guerreiro("Messi", 120, 25)

    print(heroi.atacar())
    print(mago.atacar())
    print(guerreiro.atacar())