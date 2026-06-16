class ElevadorSobrecargadoError:
    pass

class Elevador:

    def entrar_pessoa(self, peso_pessoa:float):
        self.peso_total = 0
        if    self.peso_total + peso_pessoa > 400:
            raise ElevadorSobrecargadoError("maximo 400kg")
