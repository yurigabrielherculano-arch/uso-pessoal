from random import randint

lista = []
def sorteio(lista):
    print('os numeros sorteados são: ', end='')
    for cont in range(0,5):
        n = randint(1,5)
        lista.append(n)
        print(f'{n}', end=' ')

def somapar(lista):
    soma = 0
    for s in lista:
        if s % 2 == 0:
            soma += s
    print(f'\nos numeros pares  de {lista}, somados: {soma}')
sorteio(lista)
somapar(lista)