from funcoes import *

frota_oponente = {"porta-aviões": [[[9, 1], [9, 2], [9, 3], [9, 4]]],"navio-tanque": [[[6, 0], [6, 1], [6, 2]], [[4, 3], [5, 3], [6, 3]]],"contratorpedeiro": [[[1, 6], [1, 7]], [[0, 5], [1, 5]], [[3, 6], [3, 7]]],"submarino": [[[2, 7]], [[0, 6]], [[9, 7]], [[7, 6]]]}

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}
nomes = ["porta-aviões", "navio-tanque", "contratorpedeiro", "submarino"]
tamanhos = [4, 3, 2, 1]
quantidades = [1, 2, 3, 4]
i = 0
while i < 4:
    j = 0
    while j < quantidades[i]:
        valido = False
        while valido == False:
            print("Insira as informações referentes ao navio " + nomes[i] + " que possui tamanho " + str(tamanhos[i]))

            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if i == 3:
                orientacao = "vertical"
            else:
                orientacao = int(input("Orientação: [1] Vertical [2] Horizontal "))

                if orientacao == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"

            if posicao_valida(frota, linha, coluna, orientacao, tamanhos[i]):
                frota = preenche_frota(frota, nomes[i], linha, coluna, orientacao, tamanhos[i])
                valido = True
            else:
                print("Esta posição não está válida!")
        j = j + 1
    i = i + 1
tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)
jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    linha = int(input("Jogador, qual linha deseja atacar? "))
    while linha < 0 or linha > 9:
        print("Linha inválida!")
        linha = int(input("Jogador, qual linha deseja atacar? "))
    coluna = int(input("Jogador, qual coluna deseja atacar? "))
    while coluna < 0 or coluna > 9:
        print("Coluna inválida!")
        coluna = int(input("Jogador, qual coluna deseja atacar? "))
    while tabuleiro_oponente[linha][coluna] == "X" or tabuleiro_oponente[linha][coluna] == "-":
        print("A posição linha " + str(linha) + " e coluna " + str(coluna) + " já foi informada anteriormente!")
        linha = int(input("Jogador, qual linha deseja atacar? "))
        while linha < 0 or linha > 9:
            print("Linha inválida!")
            linha = int(input("Jogador, qual linha deseja atacar? "))
        coluna = int(input("Jogador, qual coluna deseja atacar? "))
        while coluna < 0 or coluna > 9:
            print("Coluna inválida!")
            coluna = int(input("Jogador, qual coluna deseja atacar? "))
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)
    print(afundados(frota_oponente, tabuleiro_oponente))
    if afundados(frota_oponente, tabuleiro_oponente) >= 10:
        print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False
