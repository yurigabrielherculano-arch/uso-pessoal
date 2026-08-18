from random import randint
from time import sleep
sorti = []
jogos = []
num = randint(1,60)
tot = 1
print('========================================')
print('            JOGA ESSAS NA MEGA                           ')
print('========================================')
quant = int(input('quantos jogos vc quer gerar: '))
while tot <= quant:

    for c in range(0, 6):

        while num in sorti:
            num = randint(1, 60)
        sorti.append(num)
    tot += 1
    sorti.sort()
    jogos.append(sorti[:])
    sorti.clear()

print('-' *30,f'sorteando {quant} jogos','-'*30)
for i, jogo in enumerate(jogos):
    print(f'jogo {i +1}: {jogo}')
    sleep(2)
print('===== boa sorte ! =====')




