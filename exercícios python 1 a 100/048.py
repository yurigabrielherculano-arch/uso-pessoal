cont = 0
soma = 0
for s in range(1,501,2):
    if s % 3 == 0:
        soma = soma + s
        cont = cont + 1
print("a soma de todos os {} valores solicitados é {}".format(cont,soma))
     