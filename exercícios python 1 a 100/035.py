r1 = float(input("primeiro seguimemto: "))
r2 = float(input("segundo seguimemto: "))
r3 = float(input("terceiro seguimento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("os seguimentos acima formam um triangulo: ")
else:
    print("os segumentos acima não formam um triangulo")