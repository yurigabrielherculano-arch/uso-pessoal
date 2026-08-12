from datetime import date 
atual = date.today().year
nascimento = int(input("em que ano vc nasceu?"))
idade = atual - nascimento
print("nasceu no ano de {} tem {}anos em {}".format(nascimento,idade,atual))

if idade == 18:
    print("vc tem que se ALISTAR IMEDIATAMENTE")
elif idade < 18:
    saldo = 18 - idade
    print("ainda faltam {} ano/anos para seu alistamento".format(saldo))
    ano = atual + saldo
    print("seu alistamento sera em {}".format(ano))
elif idade > 18:
    saldo = idade - 18
    print("vc ja deveria ter se alistado ah {} anos".format(saldo))
    ano = atual - saldo
    print("seu alistamento deveria ter sio no de {}".format(ano))