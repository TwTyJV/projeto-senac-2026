from imagem import Imagem
from pdf import PDF

if __name__ == '__main__':

    imagem = Imagem()
    pdf = PDF ()
    for i in range(2):
        print (imagem.exibir())
        print (pdf.exibir())