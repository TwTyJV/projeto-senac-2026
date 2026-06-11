class Combinadas:

    def validar_usuario(self, nome:str):
        if len(nome) <= 3:
            raise ValueError
        return "Usuário válido."
    