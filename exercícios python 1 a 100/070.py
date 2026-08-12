tot = totmil = menor = cont = 0
barato = " "
while True:
    produto = str(input("nome do produto:")).strip().upper()
    preço = float(input("preço: R$"))
    cont += 1
    tot += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = " "
    while resp not in "SN":
        resp = str(input("quer continuar? [s/n] ")).strip().upper()[0]
    if resp == "N":
        break
print('{:-^40}'.format("fim do programa"))
print(f"o total da compra foi R$ {tot:.2f}")
print(f"temos {totmil} produtos a cima de 1000 R$")
print(f"o produto mais barato foi o {barato}")