princ = []
temp = []
maior = menor = 0
while True:
    temp.append(str(input('nome:')))
    temp.append(float(input('peso:')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('quer continuar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'ao todo temos {len(princ)} pessoas cadastradas.')
print(f'o maior peso foi {maior} kg. peso de ', end=' ')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\no menor peso foi {menor} kg.peso de ', end=' ')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')


