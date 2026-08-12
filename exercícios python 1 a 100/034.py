salario = float(input("digite seu salario atual:"))
if salario <= 1250:
    aumento = salario + (salario * 15/100)
else:
    aumento = salario + (salario * 10/100)
print("qm ganhava {:.2f} vai passar a ganhar {:.2f} agora".format(salario, aumento))