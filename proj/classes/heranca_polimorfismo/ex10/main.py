from heroi import Heroi
from guerreiro import Guerreiro
from mago import Mago

if __name__ == '__main__':

    heroi = Heroi("Cr7", 100)
    mago = Mago("Neymar", 80, 30)
    guerreiro = Guerreiro("Messi", 120, 25)

    print(heroi.atacar())
    print(mago.atacar())
    print(guerreiro.atacar())