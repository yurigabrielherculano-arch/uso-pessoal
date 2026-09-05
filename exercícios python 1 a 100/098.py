from time import sleep
def contador(i,f,p):
    print('-='*20)
    print(f'contagem de {i} ate {f} de {p}')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}',end=' ')
            sleep(0.8)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.8)
            cont -= p
        print('FIM')
print('-='*20)
contador(1,10,1)
contador(10,0,2)
print('sua vez')
inicio = int(input('inicio: '))
fim = int(input('fim: '))
passo = int(input('passo: '))
contador(inicio,fim,passo)
