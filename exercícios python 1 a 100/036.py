casa = float(input("qual o valor da casa? "))
salario = float(input("qual o seu salario? "))
anos = int(input("quantos anos de finaciamento? "))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print("para pagar um emprestimo de {:.2f} em {} anos, a prestação sera de {:.2f}".format(casa, anos,prestação))
if prestação <= minimo:
    print("emprestimo pode ser concedido,PARABENS !!")
else:
    print("emprestimo negado, sinto muito")