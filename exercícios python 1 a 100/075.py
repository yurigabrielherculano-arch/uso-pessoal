n1 = int(input('digite um numero:'))
n2 = int(input('digite outro numero:'))
n3 = int(input('outro numero:'))
n4 = int(input('outro numero:'))
jt = (n1, n2, n3, n4)
print(f'o numero digitado foi {jt}')
print(f'o numero 9 apareceu {jt.count(9)} vezes')
for pos, posi in enumerate(jt):
    if posi == 3:
        print(f'o numero 3 esta na {pos + 1 }º posição')
print(f'os numeros pares são: ', end=' ')
for numero in  jt:
    if numero % 2 == 0:
        print(numero, end=' ')