class Multiplos:

    def processar_dados(self, lista: list, indice:int):

        if indice >= len(lista):
            raise IndexError('Indice não existe')
    
        if not isinstance(lista[indice], int):
            raise TypeError('Tipo não suportado para operação matemática')
        
        return lista[indice] / 2