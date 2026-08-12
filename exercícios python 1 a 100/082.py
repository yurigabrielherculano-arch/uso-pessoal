lista = []
par = []
impar = []
while True:
    lista.append(int(input('digite um numero:')))
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('quer continuar [S/N]:')).strip()[0]
    if resp in 'Nn':
        break
for c in lista:
        if c % 2 == 0:
            par.append(c)
        elif c % 2 == 1:
            impar.append(c)
print(f'a lista completa é {lista}')
print(f'a lista par fica {par}')
print(f'a lista de impar fica {impar}')

