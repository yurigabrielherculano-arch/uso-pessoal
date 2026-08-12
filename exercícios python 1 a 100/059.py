from time import sleep
v1 = int(input("primeiro valor:"))
v2 = int(input("segundo valor"))
opção = 0
while opção != 5:
    print("""[1]soma
[2]multiplicação
[3]maior
[4]novos números
[5]sair do programa""")
    opção = int(input(">>>>qual sua opção:"))
    if opção == 1:
        soma = v1 + v2
        print("soma entre {} + {} é {}".format(v1,v2,soma))
    elif opção == 2:
        multiplicar = v1 * v2
        print("a multiplicação entre {} x {} é {}".format(v1,v2,multiplicar))
    elif opção == 3:
        if v1 > v2:
            print("o maior valor é {}".format(v1)) 
        else:
            print("o maior valor é {}".format(v2))
    elif opção == 4:
        print("informe os números novamente:")
        v1 = int(input("primeiro valor:"))
        v2 = int(input("segundo valor:"))
    elif opção == 5:
        print("processando...")
    else:
        print("opção invalida,tente novamente")
    print("-=-"*10)
    sleep(1)
print("fim do programa, volte sempre !!")