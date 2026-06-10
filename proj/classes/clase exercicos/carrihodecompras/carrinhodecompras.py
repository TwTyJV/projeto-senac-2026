class  CarrinhoDeCompras:
    itens:list
    precos:list

    def __init__(self):
        self.itens = []
        self.precos = []
    
    def adicionar_item(self, nome_produto:list, preco_produto:list): 
        self.itens.append (nome_produto)
        self.precos.append(preco_produto)

    def calcular_total(self):
        total = 0
        for preco in self.precos:
            total += preco
        return total