pessoa = {}
ficha = []
media = 0
media_idade = totm = 0
while True:
    pessoa['nome'] = str(input('nome: '))
    while True:
        pessoa['sexo'] = str(input('sexo: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('opção invalida!,digite apenas m ou f')
    pessoa['idade'] = int(input('idade: '))
    while True:
        resp = str(input('deseja continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('aviso, digite apenas S ou N, infeliz')
    ficha.append(pessoa.copy())
    pessoa.clear()
    if resp == 'N':
        break
for pessoa in ficha:
    media_idade += pessoa['idade']
    media  = media_idade / len(ficha)
for pessoa in ficha:
    if pessoa['sexo'] == 'F':
        totm += 1


print(f'A) ao todo temos {len(ficha)} pessoas cadastradas')
print(f'b) a media de idade é {media :.0f} anos')
print(f'c) as mulheres cadastradas total de {totm} elas são ',end='')
for pessoa in ficha:
    if pessoa['sexo'] == 'F':
        print(f' {pessoa["nome"]}',end='')
print()
print('lista das pessoas a cima da media')
for pessoa in ficha:
    if pessoa['idade'] >= media:
        print('         ',end='')
        for k, v in pessoa.items():
            print(f'{k} = {v},', end='')



