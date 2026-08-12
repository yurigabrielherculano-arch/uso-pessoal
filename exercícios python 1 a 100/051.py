primeiro = int(input("primeiro termo:"))
razão = int(input("razão:"))
decimo = primeiro + (10 - 1) * razão
for c in range(primeiro,decimo + razão, razão):
    print("{}".format(c), end = " -> ")
print("acabou")