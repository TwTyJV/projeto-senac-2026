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
    if lado1 + lado2 <=lado3 or lado2 + lado3 <=lado1 or lado1 + lado3 <=lado2: 
        return "não é trinagulo"
    
    if lado1 == lado2 == lado3:
        return "equilátero"
    if (lado1 != lado2 != lado3):
        return "Escaleno"
    return "isóciles"
        
def aprovar_saque(saldo:float, valor_saque:float):
    if valor_saque <= saldo and valor_saque % 10 == 0:
        return True
    return False


################# Exercícios (3ª aula) ###############def primeira_fruta(lista_de_frutas):


frutas = ['maçã', 'banana', 'laranja', 'morango']

def primeira_fruta(frutas: list):
    return frutas[0]

if __name__ == '__main__':

    fruta = primeira_fruta(frutas)
    print(fruta)




animais = ['gato', 'cachorro', 'passarinho', 'coelho']

def ultimo_animal(animais:list):
    return animais[-1]

if __name__ == '__main__':

    animal= ultimo_animal(animais)
    print(animal)


def adicionar_compras(compras: list):
    compras.append('arroz')
    compras.append('feijão')
    compras.append('batata')
    return compras
 
if __name__ == '__main__':

    compras= adicionar_compras(compras=[])
    print(compras)


notas = [7.5, 8.0, 6.0, 9.5, 10.0]

def quantidade_notas(notas: list):
    len(notas)
    return len(notas)

if __name__ == '__main__':

    notas= quantidade_notas(notas)
    print(notas)


    
    
cores = ['vermelho', 'verde', 'azul']


def mudar_cor(cores:list):
    cores[1] = 'amarelo'
    return cores

if __name__ == '__main__':

    cores= mudar_cor(cores)
    print(cores)

tarefas = ['estudar', 'limpar quarto', 'lavar louça']

def esvaziar_tarefas(tarefas:list):
    tarefas.clear()
    return(tarefas)

if __name__ == '__main__':

    tarefas = esvaziar_tarefas(tarefas)
    print(tarefas)


respostas = ['Sim', 'Não', 'Sim', 'Sim', 'Não', 'Sim']

def contar_sim(respostas:list):
    return respostas.count('Sim')
   

if __name__ == '__main__':

    respostas = contar_sim(respostas)
    print(respostas)



fila = ['Ana', 'Bruno', 'Carlos', 'Diego']

def remover_ultimo(fila:list):
    fila.pop()
    return (fila)

if __name__ == '__main__':

    fila = remover_ultimo(fila)
    print(fila)


canais = ['Globo', 'SBT', 'Record', 'Band']

def posicao_sbt(canais: list):
    return canais.index('SBT')

if __name__ == '__main__':

    canais = posicao_sbt(canais)
    print(canais)


dias = ['Segunda', 'Quarta', 'Quinta']

def ajustar_terca(dias:list):
    dias.insert(1, 'terça')
    return (dias)

if __name__ == '__main__':

    dias = ajustar_terca(dias)
    print(dias)


numeros = [10, 20, 30, 40, 50, 60]

def tres_primeiros(numeros:list):
    return numeros[0:3]

if __name__ == '__main__':

    numeros = tres_primeiros(numeros)
    print(numeros)


convidados = ['Alice', 'Bob', 'Arthur', 'Carol']

def remover_arthur(convidados:list):
    convidados.remove('Arthur')
    return (convidados)

if __name__ == '__main__':

    convidados = remover_arthur(convidados)
    print(convidados)

letras = ['A', 'B', 'C', 'D', 'E']

def inverter_lista(letras:list):
    letras.reverse()
    return (letras)

if __name__ == '__main__':

    letras = inverter_lista(letras)
    print(letras)


pontos = [45, 12, 89, 5, 23]

def ordenar_pontos(pontos:list):
    pontos.sort()
    return (pontos)

if __name__ == '__main__':

    pontos = ordenar_pontos(pontos)
    print(pontos)


valores = [12, 5, 8, 22, 9, 15]

def soma_extremos(valores:list):
    resultado = valores[0] + valores[-1]
    return (resultado)

if __name__ == '__main__':

    valores = soma_extremos(valores)
    print(valores)


ingredientes = ['ovo', 'farinha', 'açúcar', 'leite']

def tem_chocolate(ingredientes:list):
    if 'chocolate' in ingredientes:
        return True
    return False
    

if __name__ == '__main__':

    ingredientes = tem_chocolate(ingredientes)
    print(ingredientes)
     

amigos_escola = ['Pedro', 'Lucas'] 
amigos_bairro = ['Mariana', 'Julia']

def juntar_amigos(amigos_escola:list, amigos_bairro:list):
    amigos_escola.extend(amigos_bairro)
    return (amigos_escola)

if __name__ == '__main__':
    amigos_escola = juntar_amigos(amigos_escola, amigos_bairro)
    print(amigos_escola)


anos = [2018, 2019, 2020, 2021, 2022, 2023, 2024]

def ultimos_tres(anos:list):
    return anos[-3:]

if __name__ == '__main__':
    
    anos = ultimos_tres(anos)
    print(anos)

brinquedos = ['carrinho', 'boneca', 'bola', 'pião']

def remover_brinquedo_seguro(brinquedos:list, item:str):
    if item in brinquedos:
        brinquedos.remove(item)
        return brinquedos
    return 'Este brinquedo não está na lista!'
        
    
if __name__ == '__main__':

    brinquedo_removido = remover_brinquedo_seguro(brinquedos, 'pião')
    print(brinquedo_removido)
    mensagem = remover_brinquedo_seguro(brinquedos, 'lego')
    print(mensagem)


numeros_para_trocar = [1,2,3,4]
def trocar_extremos(numeros_para_trocar: list):
    numero_comeco = numeros_para_trocar[0]
    numeros_para_trocar[0] = numeros_para_trocar[-1]
    numeros_para_trocar[-1] = numero_comeco

    return numeros_para_trocar

if __name__ == '__main__':
    
    lista_extremos_trocados = trocar_extremos(numeros_para_trocar)
    print(lista_extremos_trocados)
    

