class Notas:
    def adicionar_nota_aluno(self, lista_notas:list, nova_nota:int):
        try:
            nota = float(nova_nota)

        except TypeError:
            print("Incorreto")
            return

        except ValueError:
            print("incorreto")
            return

        if nota < 0.0 or nota > 10.0:
            raise ValueError("Nota fora de (0.0 a 10.0)")
        lista_notas.append(nota)
