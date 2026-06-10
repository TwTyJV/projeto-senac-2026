from violao import Violão
from flauta import Flauta
from bateria import Bateria

if __name__ == '__main__':

    violao = Violão ()
    flauta = Flauta()
    bateria = Bateria()

    for i in range (3):
        print(violao.tocar())
        print(flauta.tocar())
        print(bateria.tocar())
        
