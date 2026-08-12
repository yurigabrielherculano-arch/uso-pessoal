from random import randint
computador = randint(0,10)
print("estou pensando em um número de 0 a 10")
print("consegue advinhar")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("qual o seu palpite? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("mais...tente novamente")
        elif jogador > computador:
            print("menos...tente novamente")
print("acertou com sucesso, o número de tentativas foi {}".format(palpites))       