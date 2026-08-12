frase = str(input("digite uma frase:")).upper().strip()
print("a letra A aparece {} vezes na frase".format(frase.count("A")))
print("a letra A aparece pela primeira vez na posição {}".format(frase.find("A")+1))
print("a letra A aparece pela ultima vez na posição {}".format(frase.rfind("A")+1))