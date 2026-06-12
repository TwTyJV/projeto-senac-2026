class Produto:
    
    nome:str
    preco:float

    def __init__(self, nome:str, preco:float):
        self.nome = nome
        self.preco = preco

        if preco <= 0:
            raise ValueError("tem que ser maior que zero")