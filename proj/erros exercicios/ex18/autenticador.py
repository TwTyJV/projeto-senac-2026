class ContaBloqueadaError:
    pass
class Autenticador:

    senha_correta = "1234"
    tentativas = 0

    def fazer_login(self, senha_digitada:int):
        
        if senha_digitada != self.senha_correta:
            self.tentativas +=1
            raise ValueError
        
        if self.tentativas == 3:
            raise ContaBloqueadaError
