from veiculo import Veiculo

class Estacionamento:

    def estacionar(self, veiculo:Veiculo, numero_vaga:int):
        self.vagas = self.vagas
        if numero_vaga < 0 or numero_vaga >= len(self.vagas):
            raise IndexError("numeros de vagas invalidas")
        
        vaga = self.vagas[numero_vaga]

        if not vaga.disponivel:
            raise