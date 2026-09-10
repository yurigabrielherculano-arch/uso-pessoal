import moedas

num = float(input('digite um numero em reais: R$'))
print(f'a metade de {moedas.moeda(num)} é {moedas.moeda(moedas.metade(num))}')
print(f'o dobro de {moedas.moeda(num)} é {moedas.moeda(moedas.dobro(num))}')
print(f'o aumento de 10% , é {moedas.moeda(moedas.aumento(num,10))} ')
print(f'diminuido 10%, é {moedas.moeda(moedas.diminui(num,10))}')

