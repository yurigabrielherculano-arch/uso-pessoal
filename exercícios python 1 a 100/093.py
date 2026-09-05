partida = {}
acumulador = []
partida['nome'] = str(input('nome do jogador: ')).strip().upper()
partida['jogo'] = int(input('quantas partidas: '))
for p in range(0,partida['jogo']):
    acumulador.append(int(input(f'quantos gols {p}: ')))
    partida['gols'] = acumulador[:]
toto = sum(partida['gols'])
partida['total'] = toto
print('-'*30)
print(partida)
print('-'*30)
for k,v in partida.items():
    if partida['jogo'] != v:
        print(f'o campo {k} tem valor {v} ')
print('-='*30)
print(f'O JOGADOR {partida["nome"]} JOGOU {partida["jogo"]} PARTIDAS!')
for i,v in enumerate(partida['gols']):
    print(f' => na {i}° partida, tem {v} gol ')
print(f'foi um total de {partida["total"]} gols')

