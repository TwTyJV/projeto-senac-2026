from proj.heranca_polimorfismo.ex9.funcionario import Funcionario 
from proj.heranca_polimorfismo.ex9.gerente import Gerente

if __name__ == '__main__':

    funcionario = Funcionario()
    gerente = Gerente()

    print(funcionario.trabalhar())
    print(gerente.trabalhar())
    