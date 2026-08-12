cont = (
"zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quartoze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte"
)
e = int(input("digite um número de 0 a 20:"))
while e < 0 or e > 20:
    print("erro...tente de novo!")
    e = int(input("digite um número de 0 a 20:"))
print(f"o número digitado foi {cont[e]}")