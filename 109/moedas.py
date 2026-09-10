def metade(n=0,formato=False):
    return n * 1/2 if formato is False else moeda(n)



def dobro(n=0,formato=False):
    return n * 2 if formato is False else moeda(n)


def aumento(preço=0,taxa=0,formato=False):
    aum = preço + (preço *taxa/100)
    return aum if formato is False else moeda(aum)


def diminui(preço=0,baixa=0,formato=False):
    tai = preço - (preço * baixa / 100)
    return tai if formato is False else moeda(tai)


def moeda(preço=0,moeda='R$',formato=False):
    return f'{moeda}{preço:.2f}'.replace('.',',')



