tot18 = toth = totm20 = 0
while True:
    idade = int(input("digite sua idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("digite seu sexo [M/F]: ")).upper().strip()[0]
        resp = str(input("quer continuar? [s/n] ")).upper().strip()[0]
        if idade >= 18:
            tot18 += 1
        if sexo == "M":
            toth += 1
        if sexo == "F" and idade < 20:
            totm20 += 1
    if resp == "N":
       break
print(f"o total de pessoas com mais de 18 anos foi {tot18}")
print(f"o total de mulheres com menos de 20 anos foi {totm20}")
print(f"o total de homens cadastrados com sucesso foi {toth}")