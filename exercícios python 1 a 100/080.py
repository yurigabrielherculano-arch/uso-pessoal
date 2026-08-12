lista = []
for c in range(0, 5):
    v1 = int(input('digite um valor: '))
    if c == 0 or v1 > lista[len(lista)-1]:
        lista.append(v1)
    else:
        pos = 0
        while pos < len(lista):
            if v1 <= lista[pos]:
                lista.insert(pos, v1)
                break
            pos += 1
print(f'os valores digitados foram {lista}')