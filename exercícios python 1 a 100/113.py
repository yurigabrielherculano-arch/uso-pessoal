def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mporfavor digite umm numero inteiro valido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0;31musuario não quis informa um numero\033[m')
            return 0
        else:
            return n
def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))

        except (ValueError,TypeError):
            print('\033[0;31mporfavor digite um numero real valido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0;31mo usuario não quis informa um numero\033[m')
            return 0
        else:
            return n
m = leiaint('digite um numero inteiro:')
n = leiafloat('digite um numero real:')
print(f'o numero real digitado foi {n} e inteiro {m}')
