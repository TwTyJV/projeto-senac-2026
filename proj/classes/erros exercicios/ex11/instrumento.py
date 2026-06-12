class AnatomiaError(Exception):
    pass


class Instrumento:
    def tocar(self):
        raise AnatomiaError("Classes abstratas não tocam som.")


class Guitarra(Instrumento):
    def tocar(self):
        return "A guitarra está tocando um riff!"


def testar_instrumento(inst):
    try:
        resultado = inst.tocar()
        print("Som:", resultado)
    except AnatomiaError as e:
        print("Erro:", e)


instrumento_base = Instrumento()
guitarra = Guitarra()

testar_instrumento(instrumento_base)
testar_instrumento(guitarra)