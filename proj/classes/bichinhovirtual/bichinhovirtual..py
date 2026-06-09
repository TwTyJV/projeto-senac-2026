class BichinhoVirtual:
    nome:str
    fome:int = 50
    felicidade:int = 50

    def __init__(self,nome:str, fome:int = 50,  felicidade:int = 50):
        self.nome = nome
        self.fome = 50
        self.felicidade = 50

    def alimentar(self): 
        if self.fome -15 < 0:
            self.felicidade = self.felicidade +5 

    def brincar(self):
        if self.felicidade + 20 < 100:
            self.fome = self.fome +10