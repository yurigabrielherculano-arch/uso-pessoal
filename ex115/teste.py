from biblioteca.system import *
from biblioteca.arquivo import *
from time import sleep

arq = 'cadastro.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resp = menu (['ver pessoas caastradas','cadastrar nova pessoa','sair do sistema'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        cabeçario('NOVO CADASTRO')
        nome = str(input('nome da pessoa:'))
        idade = leiaint('idade da pessoa:')
        cadastrar(arq,nome,idade)
    elif resp == 3:
        cabeçario('saindo do sistema ate logo...!')
        break
    else:
        print('\033[0;31mporfavor digite um numero inteiro valido\033[m')
    sleep(0.5)
