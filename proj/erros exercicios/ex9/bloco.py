class Bloco:

    def simular_banco_de_dados(self,comando:str):
        if self.comando == comando:
            raise Exception ("Comando SQL inválido!")