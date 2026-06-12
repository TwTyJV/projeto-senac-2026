class Autenticador:

    def fazer_login(self, senha_digitada:int):
        self.senha_correta = "1234"
        self.tentativas = 0

        if self.tentativas == 1:
            raise ValueError
        
        if self.tentativas == 3:
            return ('ContaBloqueadaError.')
