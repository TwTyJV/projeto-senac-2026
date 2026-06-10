from funcionario import Funcionario 
from gerente import Gerente

if __name__ == '__main__':

    funcionario = Funcionario()
    gerente = Gerente()

    print(funcionario.trabalhar())
    print(gerente.trabalhar())
    