from proj.heranca_polimorfismo.ex1.veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, marca, ano):
        super().__init__(marca, ano)