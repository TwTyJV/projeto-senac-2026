from jogador import Jogador

if __name__ == '__main__':

    jogador = Jogador('joão')
    jogador.acertou_alvo(3)
    jogador.acertou_alvo(10)
    print(f"Pontuação Total: {jogador.pontuação} pontos")