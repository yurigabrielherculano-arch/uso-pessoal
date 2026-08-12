preço = float(input("preço das compras: R$"))
print("""qual a forma de pagamento:
[1]dinheiro/cheque
[2]cartão a vista
[3]2x no cartão
[4]3x ou mais no cartão""")
opção = int(input("opção de pagamento:"))
if opção == 1:
    final = preço - (preço * 10 / 100)
elif opção == 2:
    final = preço - (preço * 5 / 100)
elif opção == 3:
    final = preço
    parcela = final / 2
    print("sua parcela sera 2x de R${:.2f}".format(parcela))
elif opção == 4:
    final = preço + (preço * 20 / 100)
    parcela = final / 3
    print("sua parcela sera 3x de R${:.2f}com juros".format(parcela))
else:
    print("invalido")
print("sua compra de R${:.2f} vai custar R${:.2f} no final".format(preço,final))
