somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho =""
totmulher20 = 0
for p in range(1,5):
    print("---- {}° pessoa ----".format(p))
    nome = str(input("nome:"))
    idade = int(input("idade:"))
    genero = str(input("genero[M/F]:")).strip()
    somaidade += idade 
    if p == 1 and genero in "Mm":
        maioridade = idade
        nomevelho = nome
    if genero in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if genero in "Ff" and idade < 20:
        totmulher20 = 1
somaidade = somaidade / 4
print("a media do grupo é {} anos".format(somaidade))
print("o homem mais velho tem {} anos e se chama {}".format(maioridadehomem,nomevelho))
print("o total de {} mulheres com menos de 20 anos".format(totmulher20))