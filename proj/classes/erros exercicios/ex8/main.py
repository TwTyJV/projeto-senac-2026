from produto import Produto

if __name__ == '__main__':

    try:
        produto = Produto('japão', -1)

        print(produto.nome)
        print(produto.preco)

    except ValueError:
        print('Não pode ser menor que zero')