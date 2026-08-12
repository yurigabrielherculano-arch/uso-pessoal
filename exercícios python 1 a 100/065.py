resp = "S"
soma = quant = media = maior = menor = 0
while resp in "Ss":
    num = int(input("digite um numero:"))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("quer continuar? [S/N] ")).upper().strip()[0]
media = soma / quant
print(f"tem {quant} numeros, e a soma deles é {soma} e a media é {media}")
print(f"o maior numero é {maior} e o numero é {menor}")