import moedas

num = float(input('digite um numero em reais: R$'))
print(f'a metade de {moedas(num)} é {moedas.metade(num,True)}')
print(f'o dobro de {moedas(num)} é {moedas.moeda(moedas.dobro(num,True))}')
print(f'o aumento de 10% , é {moedas.aumento(num,10,True)} ')
print(f'diminuido 10%, é {moedas.diminui(num,10,True)}')
