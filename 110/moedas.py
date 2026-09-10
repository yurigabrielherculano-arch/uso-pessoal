def metade(preço=0,formato=False):
    n = preço * 1/2
    return n if formato is False else moeda(n)



def dobro(preço=0,formato=False):
    res = preço * 2
    return res if not formato  else moeda(res)


def aumento(preço=0,taxa=0,formato=False):
    res = preço + (preço *taxa/100)
    return res if formato is False else moeda(res)


def diminui(preço=0,baixa=0,formato=False):
    tai = preço - (preço * baixa / 100)
    return tai if formato is False else moeda(tai)


def moeda(preço=0,moeda='R$',formato=False):
    return f'{moeda}{preço:.2f}'.replace('.',',')


def resumo(preço=0,taixa=10,taxa=10):
    print('-='*30)
    print('ANALISANDO RESUMIDAMENTE'.center(30))
    print('-='*30)
    print(f'analisando: \t\t\t{moeda(preço)}')
    print(f'o dobro é:  \t\t\t{dobro(preço,True)}')
    print(f'a metade é: \t\t\t{metade(preço,True)}')
    print(f'{taixa}% o aumento é: \t\t{aumento(preço,taixa,True)}')
    print(f'{taxa} diminuindo fica: \t{diminui(preço,taxa,True)}')