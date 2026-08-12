n = int(input("digite um numero :"))
print("""escolha 
[1]para decimal
[2]para octal
[3]para hexadecimal""")
opcao = int(input("qual sua opcao:"))
if opcao == 1:
    print(bin(n)[2:])
elif opcao == 2:
    print(oct(n)[2:])
elif opcao == 3:
    print(hex(n)[2:])
    