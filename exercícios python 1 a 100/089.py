ficha = []
while True:
    nome = str(input('nome do aluno: '))
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('deseja continuar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
print('-='*30)
print(f'{'nO ':<4}{'nome': <10}{'media ': >8}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>6.1f}')
while True:
    opc = int(input('quer mostrar nota de qual aluno? [999] para parar: '))
    if opc == 999:
        print('finalizando...')
        print('acabou')
        break
    if opc <= len(ficha) - 1:
        print(f'notas de {ficha [opc] [0]} são {ficha[opc][1]}')