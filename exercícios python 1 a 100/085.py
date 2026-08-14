dado = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'digite o {c}° valor: '))
    if valor % 2 == 0:
        dado[0].append(valor)
    else:
        dado[1].append(valor)
print('-='*30)
dado[0].sort()
dado[1].sort()
print(f'os valores pares são {dado[0]}')
print(f'os valores impares são {dado[1]}')
