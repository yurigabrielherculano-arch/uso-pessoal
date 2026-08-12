from datetime import date
ano = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,8):
    nasci = int(input("digite a data de nascimento {}° pessoa: ".format(c)))
    idade = ano - nasci
    if idade >= 21:
        totmaior +=1
    else:
        totmenor += 1
print("o total de pessoas maiores de idade é {}".format(totmaior))
print("o total de pessoas menores de idade é {}".format(totmenor))