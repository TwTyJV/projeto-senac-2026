from conta import Conta

class Contaestudante(Conta):

    def render_bonus(self):
        self.saldo += 10
            