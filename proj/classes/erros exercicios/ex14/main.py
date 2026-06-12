from elevador import Elevador, ElevadorSobrecargadoError

if __name__ == '__main__':

   elevador = Elevador()

try:
   print(elevador.entrar_pessoa(300))
   print(elevador.entrar_pessoa(200))
except ElevadorSobrecargadoError: print ("Maximo de peso 400kg")