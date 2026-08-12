lista = ('lapis',1.70,
         'caderno',34.90,
         'borracha',4.40,
         'caneta',10,
         'corretivo',20.70)
for pos in range(0,len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}',end='')
    else:
        print(f'R${lista[pos]:>3}')