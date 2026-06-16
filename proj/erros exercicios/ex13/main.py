from notas import Notas

if __name__ == '__main__':

    notas = Notas()
     
    try:
        print(notas.adicionar_nota_aluno([],15))
    except ValueError : 
        print("A nota tem que ser entre 0.0 a 10.00")