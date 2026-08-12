velocidade = float(input("qual a velocidade atual do carro? "))
if velocidade > 80:
    print("MULTADO!! você ultrapassou o limite de velocidade que é 80hm/h")
    multa = (velocidade-80) *7
    print("você tera de R${}".format(multa))
print("tenha um bom dia dirija com cuidado")
