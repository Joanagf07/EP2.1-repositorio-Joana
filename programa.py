from funcoes import *
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

while i < len(nomes):
    j = 0

    while j < quantidades[i]:

        valido = False

        while valido == False:

            print("Insira as informações referentes ao navio " + nomes[i] + " que possui tamanho " + str(tamanhos[i]))

            linha = int(input())
            coluna = int(input())

            if nomes[i] == "submarino":
                orientacao = "vertical"
            else:
                orientacao = int(input())

                if orientacao == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"

            if posicao_valida(frota, linha, coluna, orientacao, tamanhos[i]):
                frota = preenche_frota(frota, nomes[i], linha, coluna, orientacao, tamanhos[i])
                valido = True
            else:
                print("Esta posição não está válida!")

        j = j+1

    i = i+1

print(frota)