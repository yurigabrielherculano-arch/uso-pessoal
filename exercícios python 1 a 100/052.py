num = int(input("digite um numero:"))
cont = 0
for c in range(1,num+1):
    if num % c == 0:
        print("\033[33m", end = " ")
        cont = cont + 1
    else:
        print("\033[31m", end = " ")
    print("{}".format(c), end = " ")
print("\n\033[mo numero {} foi dividido {} vezes".format(num,cont))
if cont == 2:
    print("é primo")
else:
    print("não é primo")