class Multiplos:

    def processar_dados(self, lista:list, indice:int):

        try:
            elemento = lista[indice] / 2
        except IndexError