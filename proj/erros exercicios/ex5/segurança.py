class Segurança:

    def obter_elemento(self, lista:list, indice:int):
        try:
            return lista[indice]
        except IndexError:
            return("Posição inexistente.")