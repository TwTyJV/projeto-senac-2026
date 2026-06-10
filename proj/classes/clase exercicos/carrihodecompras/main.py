from carrinhodecompras import CarrinhoDeCompras

if __name__ == '__main__':

    carrinhodecompras = CarrinhoDeCompras()
    carrinhodecompras.adicionar_item("chuteira", 550.0)
    print(CarrinhoDeCompras.calcular_total)