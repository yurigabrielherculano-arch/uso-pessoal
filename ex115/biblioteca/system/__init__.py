def linha(tam= 30):
    return '-'*tam


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


def cabeçario(txt):
    print(linha())
    print(txt.center(30))
    print(linha())


def menu(lista):
    cabeçario('MENU PRINCIPAL')
    c =1
    for item in lista:
        print(f'\033[33m{c}\033[m → \033[34m{item}\033[m')
        c +=1
    print(linha())
    opc = leiaint('\033[32msua opção: \033[m')
    return opc