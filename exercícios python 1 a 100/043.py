peso = float(input("qual o seu peso?"))
alt = float(input('qual a sua altura?'))
imc = peso / (alt ** 2)
print("seu IMC é {:.1f}".format(imc))
if imc < 18.5:
    print("abaixo do peso")
elif imc >= 18.5 and imc <= 25:
    print("peso ideal")
elif imc >= 25 and imc<= 30:
    print("sobrpeso")
elif imc >= 30 and imc <= 40:
    print("obesidade")
else:
    print("obesidade morbida")