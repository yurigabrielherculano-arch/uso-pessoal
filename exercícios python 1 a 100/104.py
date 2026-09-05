def leiaint(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('\033[0;31mErro! comando invalido!\033[m')


    return valor
n = leiaint('digite um numero inteiro: ')
print(f'o numero digitado foi {n}')