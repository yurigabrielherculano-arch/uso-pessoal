from random import randint
n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'os numeros sorteados são:',end = ' ')
for c in n:
    print(f'{c} ',end = ' ')

print(f'\no maior numero sorteado é {max(n)}')
print(f'o menor numero sorteado é {min(n)}')
