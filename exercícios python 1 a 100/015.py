dias = int(input("quantos dias alugados?"))
km = float(input("quantos hm rodados?"))
pago = (dias *60) + (km * 0.15)
print("total a pagar é de R${}".format(pago))