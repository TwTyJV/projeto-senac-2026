from contabancaria import Contabancaria, SaldoInsuficienteError

def processar_lote_saques(conta_objeto, lista_de_valores):
    saques_nao_executados = []
    
    for index, valor in enumerate(lista_de_valores):
        try:
            conta_objeto.sacar(valor)
        except TypeError:
            print("Aviso: Valor inválido.")
            continue
        except SaldoInsuficienteError:
            saques_nao_executados = lista_de_valores[index:]
            break
            
    return saques_nao_executados

if __name__ == '__main__':
    conta = Contabancaria("joao", 1000)
    lote_saques = [100, 50, "abc", 200, 300, 50]    
    
    nao_executados = processar_lote_saques(conta, lote_saques)
