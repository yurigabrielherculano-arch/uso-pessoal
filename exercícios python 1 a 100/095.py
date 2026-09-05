partida = {}
acumulador = []
time = []
while True:
    partida.clear()
    partida['nome'] = str(input('nome do jogador: ')).strip().upper()
    acumulador.clear()
    partida['jogo'] = int(input('quantas partidas: '))
    for p in range(0,partida['jogo']):
        acumulador.append(int(input(f'quantos gols {p}: ')))
        partida['gols'] = acumulador[:]
    toto = sum(partida['gols'])
    partida['total'] = toto
    time.append(partida.copy())
    while True:
        resp = str(input('quer continuar [S/N]? ')).upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-'*30)
print('cod',end='')
for i in partida.keys():
    print(f'{i:<15} ',end='')
print()
print('-'*30)
for k,v in enumerate(time):
    print(f'{k:<3} ',end='')
    for d in v.values():
        print(f'{str(d):<15} ',end='')
    print()
print('-'*30)
while True:
    busca = int(input('mostar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print('erro jogador não encontrado')
    else:
        print(f'levantamento do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'     no jogo {i + 1} fez {g} gols ')
        print('-='*30)
print('fim')