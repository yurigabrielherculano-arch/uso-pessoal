primeiro = int(input("primeiro:"))
razão = int(input("segundo:"))
termo = primeiro
cont = 0
while cont < 10:
    print(f"{termo} ->" , end = "")
    termo = termo + razão
    cont += 1
print("fim")