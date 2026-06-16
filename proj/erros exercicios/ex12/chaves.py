class Chaves:

    def buscar_letra_na_lista(self, lista_de_strings:list, indice_lista:int, indice_palavra:int):
        try:
            palavra = lista_de_strings[indice_lista]
            letra = palavra[indice_palavra]
            return letra
        except IndexError as erro:
            print(str(erro))
            return ("não foi possível acessar a letra")