from usuario import Usuario
from admin import Admin
from comum import Comum

def deletar_banco_de_dados(usuario_objeto: Usuario):
    if not isinstance(usuario_objeto, Admin):
        raise PermissionError("Acesso negado")
        
if __name__ == '__main__':

    admin = Admin()
    comum = Comum()
    try:
        print(deletar_banco_de_dados(comum))
    except:
        print('Acesso negado')

    