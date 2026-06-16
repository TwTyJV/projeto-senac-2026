from proj.heranca_polimorfismo.ex9.funcionario import Funcionario

class Gerente(Funcionario):

    def trabalhar(self):
        return super().trabalhar() + 'e revisando relatórios da equipe.'