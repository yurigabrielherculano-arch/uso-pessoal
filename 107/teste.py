import moeda

num = float(input('digite um numero em reais: R$'))
print(f'a metade de R${num} é {moeda.metade(num)}')
print(f'o dobro de R${num} é {moeda.dobro(num)}')
print(f'o aumento de 10% , é R${moeda.aumento(num,10)} ')
print(f'diminuido 10%, é R${moeda.diminui(num,10)}')

