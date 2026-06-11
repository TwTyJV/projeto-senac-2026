from heroi import Heroi

class Mago(Heroi):
    def __init__(self, nome, vida, poder_magico):
        super().__init__(nome, vida)
        self.poder_magico = poder_magico

    def atacar(self):
        return self.poder_magico + 10