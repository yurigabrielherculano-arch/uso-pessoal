def escreva(msg):
    tam = len(msg)
    print('~' * tam)
    print(f'{msg}')
    print('~' * tam)

msg = str(input('qual a mensagem desejada: '))
escreva(msg)


# no len(msg) pode botar +2 ou 4 depende do tamanho que vc quer que termine.