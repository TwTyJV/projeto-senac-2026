from espada import Espada  
from inventario import Inventario, InventarioCheioException ,ItemInutilException
from item import Item
from pedracomum import PedraComum
from pocao import Pocao

if __name__ == '__main__':

    inventario = Inventario()

try:
    inventario.guardar_item(Espada())
    inventario.guardar_item(Pocao())
    inventario.guardar_item(Espada())
    inventario.guardar_item(Pocao())

except InventarioCheioException as e:
    print('inventario cheio')

except ItemInutilException as e:
    print("item ruim")