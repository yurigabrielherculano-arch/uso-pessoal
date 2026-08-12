primeiro = int(input("primeiro termo:"))
razão = int(input("segundo termo:"))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <=total:
        print(f"{termo} ->", end = "")
        termo += razão
        cont += 1
    print("pausa")
    mais = int(input("quer mais um termo? "))
print(f"progressão terminada com {total}termos")