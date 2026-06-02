################# Exercícios (1ª aula) #################

def calcula_area_triangulo(base: float, altura: float):
    area = (base * altura) / 2
    print(f"A área do triângulo é: {area}")

def converte_temperatura_fahrenreit(graus_celsius: float):
    temperatura = (graus_celsius * (9/5)) + 32
    print(f"A temperatura em fahrenreit é: {temperatura}")

def converte_em_dolares(reais: float):
    dolares = reais / 5.04
    print(f"O valor em dólares é: {dolares}")


    ################# Exercícios (2ª aula) #################

def classificar_pop(idade: int) -> str: 

    if idade <= 12:
        return "Criança"
    
    if idade > 12 and idade <18:
        return "Adolescente"
    
    if idade > 18 and idade <= 60:
        return "Adulto"
    
    else:
        return "idoso"
    

    ############################################################

def he_par(number: int):
    if number%2 == 0:
        return True
    return False

def classificar_idade(idade: int):
    if idade <=12:
        return "criança"
    if idade >12 and idade <=17:
        return "adolescente"
    if idade >18:
        return "adulto"
    
    def calcular_bonus(salario: float, anos_empresa: int):
        if anos_empresa <= 5:
            return salario * 0.05
        else:
            return salario * 0.10
        

def encontrar_maior(a:int, b:int, c:int):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    else:
        return c

def tipo_triangulo(lado1:float, lado2:float, lado3:float):
    if lado1 + lado2 <=lado3 or lado2 + lado3 <=lado1 or lado1 + lado3 <=lado2: return "não é trinagulo"
    
    if lado1 == lado2 == lado3:
        return "equilátero"
     
     if lado1 == lado2 or lado1 == lado3 or lado2 == lado3: return "isosiles"
    
    esle:
        return:"escaleno"
        

         