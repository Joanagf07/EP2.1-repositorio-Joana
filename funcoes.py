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

