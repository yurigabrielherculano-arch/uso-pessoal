palavras = ('programar','correr','socorrer','jogar','beber',)
for p in palavras:
    print(f'\nna palavrea {p} temos ',end='')
    for letra in p:
        if letra.lower()in 'aeiou':
            print(letra,end='')