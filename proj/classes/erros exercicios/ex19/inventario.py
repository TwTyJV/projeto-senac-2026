from item import Item
from pedracomum import PedraComum

class ItemInutilException:
    pass


class InventarioCheioException:
    pass


class Inventario(Item):

    def __init__(self):
        self.itens = []

    def guardar_item(self, objeto_item):
        if not isinstance(objeto_item, Item):
            raise TypeError("O objeto deve ser derivado de Item.")

        if type(objeto_item) is PedraComum:
            raise ItemInutilException(
                "Pedras comuns não podem ser armazenadas."
            )

        if len(self.itens) > 3:
            raise InventarioCheioException(
                "O inventário está cheio."
            )

        self.itens.append(objeto_item)