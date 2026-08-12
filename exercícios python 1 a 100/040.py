a = float(input("digite a primeira nota:"))
b = float(input("digite a segunda nota:"))
media = (a + b) / 2
print("entre a {:.2f} nota e a {:.2f} nota a media é {}".format(a,b,media))
if media < 5:
    print("reprovado")
elif media >= 5 and media < 7:
    print("recuperação")
else:
    print("aprovado")