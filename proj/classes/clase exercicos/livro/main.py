from livro import Livro

if __name__ == '__main__':
    livro = Livro ("Internacional 2006","João", 10)
    livro.vender()
    print(livro.quantidade_copias)