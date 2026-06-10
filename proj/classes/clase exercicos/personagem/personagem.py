class Personagem:

    nome:str
    vida:int
    ataque:int

    def __init__(self, nome:str, vida:int, ataque:int ):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def esta_vivo(self):
        if self.vida >0 :
            return True
        return False
    
    def receber_dano(self, quantidade):
        self.vida -= quantidade
        if self.vida < 0:
            self.vida = 0

    def atacar(self, oponente):
      if self.esta_vivo():
        oponente.receber_dano(self.ataque)

    