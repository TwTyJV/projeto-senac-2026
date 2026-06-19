def registrar_pontuacao(nome_jogador:str, pontos:int):
    with open('ranking.txt', 'a') as arquivo:
        arquivo.write(f"Nome: {nome_jogador}, Pontos: {pontos}")