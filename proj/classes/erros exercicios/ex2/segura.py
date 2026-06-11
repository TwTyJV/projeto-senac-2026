class Segura:

    def converter_para_inteiro(self,texto:str):
        try:
            numero = int(texto)
        except Exception as e:
            return 'Conversão inválida'
        
        return numero
