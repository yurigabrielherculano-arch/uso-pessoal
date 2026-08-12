a = int(input("digite um valor: "))
b = int(input("digite o segundo valor: "))
c = int(input("digite o terceiro valor: "))
menor = a
if b < a and b < c:
    menor = b
if c < a and b < c:
    menor = c
maior = a 
if b > a and b > c:
    maior = b
if c > b and c > b:
    maior = c
print("o menor valor é {}".format(menor))
print("o maior valor é {}".format(maior))