valores = []
for cont in range(0,5):
    valores.append(int(input(f'digite um valor da posição {cont}: ')))
print(f'os digitados foi {valores}')
print(f'o menor valor digitado foi {min(valores)} na posição ',end='')
for pos, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{pos}',end='')
print(f'\no maior valor digitado foi {max(valores)} na posição ',end='')
for pos,valor in enumerate(valores):
    if valor == max(valores):
        print(f'{pos}')
