class Lampada:

    ligada:bool


    def __init__(self):
        self.ligada = False

    def clicar_interruptor(self):
        if not self.ligada:
            self.ligada = True
        else:
            self.ligada = False

    def status(self):
        if self.status:
            self.ligada = "A lâmpada está ligada"
        else:
            self.ligada = "A lâmpada está desligada"