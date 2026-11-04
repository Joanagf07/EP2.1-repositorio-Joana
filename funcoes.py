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
