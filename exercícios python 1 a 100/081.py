lista = []
while True:
    lista.append(int(input('informe um valor:')))
    resp = str(input('quer continuar [S/N]:')).strip()[0]
    if resp in 'Nn':
        break
print(f'os valores digitados tem {len(lista)} elmentos')
lista.sort(reverse = True)
print(f'os valores decrecentes são {lista}')
if 5 in lista:
    print('o numero 5 esta na lista')
else:
    print('o numero 5 não se encontra na lista')
