from proj.heranca_polimorfismo.ex4.dispositivo import Dispositivo

class Celular(Dispositivo):

    def __init__(self, nome, bateria):
        super().__init__(nome)
        self.bateria = bateria