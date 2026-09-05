from random import randint
from operator import itemgetter

dado = {'jogador1':randint(1,6),
        'jogador2':randint(1,6),
        'jogador3':randint(1,6),
        'jogador4':randint(1,6)}
rank = []
print('valores sorteados:')
print('-'*30)
for k, v in dado.items():
    print(f'{k} tirou = {v}')
print('-'*30)
rank = sorted(dado.items(),key= itemgetter(1),reverse=True)
print('rank')
for i, v in enumerate(rank):
    print(f'{i + 1}° {v[0]} tirou {v[1]}')

