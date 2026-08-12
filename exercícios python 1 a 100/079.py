lista = []

while True:
    v1 = int(input('digite um valor: '))
    if v1 not in lista:
        lista.append(v1)
        print('VALOR ADCIONADO COM SUCESSO!')
    else:
        print('valor duplicado..... não sera adicionado')
    continua = str(input('quer continuar? [S/N] ')).strip().upper()[0]
    while continua not in 'SsNn':
        continua = str(input('quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('-=-'*20)
print(f'vc digitou os valores {sorted(lista)}')