def define_posicoes(l,c,o,t):
    i= 0
    resultado=[]
    while i<t:
        if o=="vertical":
            p=[l+i, c]
        elif o=="horizontal":
            p = [l, c+i]
        resultado.append(p)
        i = i+1
    return resultado

def preenche_frota(f,n,l,c,o,t):
    p = define_posicoes(l,c,o,t)
    if n in f:
        f[n].append(p)
    else:
        f[n] = [p]
    return f

def faz_jogada(t,l,c):
    if t[l][c]==0:
        t[l][c]="-"
    elif t[l][c]==1:
        t[l][c]="X"
    return t

def posiciona_frota(f):
    tabuleiro = []
    i = 0
    while i < 10:
        tabuleiro.append([0]*10)
        i = i+1
    for a in f:
        i = 0
        while i < len(f[a]):
            j = 0
            while j < len(f[a][i]):
                tabuleiro[f[a][i][j][0]][f[a][i][j][1]] = 1
                j = j+1
            i = i+1
    return tabuleiro

def afundados(f,t):
    total = 0
    for a in f:
        i = 0
        while i < len(f[a]):
            j = 0
            acertou = True
            while j < len(f[a][i]):
                if t[f[a][i][j][0]][f[a][i][j][1]] != "X":
                    acertou = False
                j = j+1
            if acertou == True:
                total = total+1
            i = i+1
    return total

def posicao_valida(f,l,c,o,t):
    p = define_posicoes(l,c,o,t)
    for a in p:
        if a[0]<0 or a[0]>9 or a[1]<0 or a[1]>9:
            return False
    for a in f:
        i = 0
        while i < len(f[a]):
            j = 0
            while j < len(f[a][i]):
                if f[a][i][j] in p:
                    return False
                j = j+1
            i = i+1
    return True