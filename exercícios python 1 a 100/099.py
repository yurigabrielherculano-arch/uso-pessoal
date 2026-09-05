from time import sleep
def maior(*num):
    cont = maior = 0
    print('-='*30)
    print('analisando.....')
    for valor in num:
        print(f'{valor}', end= ' ')
        sleep(1)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'os valores informados foram { cont}')
    print(f'o maior valor informado foi {maior}')



maior(2,9,6,7,8,4)
maior(1,4,7)
maior(6)
maior()