num = cont = soma = 0
num = int(input("digite um numero [999 para parar]:"))
while num != 999:
    soma += num
    cont += 1
    num = int(input("digite um numero [999 para parar]:"))
print(f"o total de numeros usados foi {cont}, e a soma entre eles é {soma}")