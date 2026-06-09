class Jogador:

    nome:str
    pontuação:int = 0

    def __init__(self, nome:str,pontuação:int = 0):
        self.nome = nome
        self.pontuação = 0

    def acertou_alvo(self, distancia_do_centro:float):
        if distancia_do_centro < 5:
            return 100
        if 5 <= distancia_do_centro <= 20:
            return 50
        if distancia_do_centro > 20:
            return 10
        
