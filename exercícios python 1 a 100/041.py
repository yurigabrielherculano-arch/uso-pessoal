from datetime import date
atual = date.today().year
nascimento = int(input("digite o ano de nascimento:"))
idade = atual - nascimento
print("o atleta tem {} anos".format(idade))
if idade <= 9:
    print("classificação: mirim")
elif idade <= 14:
    print("classificação: infantil")
elif idade <= 19:
    print("classificação: junuir")
elif idade <= 25:
    print("classificação: sênior")
else:
    print("classificação: master")