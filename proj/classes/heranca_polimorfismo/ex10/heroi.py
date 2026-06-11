class Heroi:

    nome:str
    vide:int


    def __init__(self, nome:str, vida:int):
        self.nome = nome
        self.vida = vida

    def atacar(self):
        return "Não há arma para atacar."