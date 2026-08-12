quant = soma = 0
while True:
    n = int(input("digite um numero: [999 para parar] "))
    if n == 999:
        break 
    soma += n
    quant += 1
print(f"a soma é {soma} e a quantidade usada foi {quant}")