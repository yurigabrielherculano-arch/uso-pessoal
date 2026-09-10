def metade(n):
    return n * 1/2



def dobro(n):
    return n * 2


def aumento(preço,taxa):
    aum = preço + (preço *taxa/100)
    return aum


def diminui(preço,baixa):
    tai = preço - (preço * baixa / 100)
    return tai


def moeda(preço=0,moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

