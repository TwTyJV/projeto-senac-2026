from proj.heranca_polimorfismo.ex10.heroi import Heroi

class Guerreiro(Heroi):
    def __init__(self, nome, vida, forca_fisica):
        super().__init__(nome, vida)
        self.forca_fisica = forca_fisica

    def atacar(self):
        return self.forca_fisica * 2