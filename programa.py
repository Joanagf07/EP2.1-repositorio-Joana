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

        print("Insira as informações referentes ao navio " + nomes[i] + " que possui tamanho " + str(tamanhos[i]) + "; A quantidade e o tamanho das embarcação são definidas pela tabela a seguir:")

        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))

        if nomes[i] == "submarino":
            orientacao = "vertical"
        else:
            orientacao = int(input("Digite a orientação (1 - vertical, 2 - horizontal): "))

            if orientacao == 1:
                orientacao = "vertical"
            else:
                orientacao = "horizontal"

        while posicao_valida(frota, linha, coluna, orientacao, tamanhos[i]) == False:
            print("Esta posição não está válida!")

            linha = int(input("Digite a linha: "))
            coluna = int(input("Digite a coluna: "))

            if nomes[i] != "submarino":
                orientacao = int(input("Digite a orientação (1 - vertical, 2 - horizontal): "))

                if orientacao == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"

        frota = preenche_frota(frota, nomes[i], linha, coluna, orientacao, tamanhos[i])

        j = j+1

    i = i+1

print(frota)