sexo = str(input("digite seu sexo [m/f]:")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("dado invalido,por favor digite seu sexo [m/f]:".format(sexo))).strip().upper()[0]
print("sexo {} registrado com sucesso".format(sexo))