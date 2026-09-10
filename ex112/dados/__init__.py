def leiadinheiro(msg):
    validade = False
    while not validade:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" VALOR INVALIDO!\033[m')
        else:
            validade= True
            return float(entrada)