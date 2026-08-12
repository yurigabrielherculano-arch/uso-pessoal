from random import randint
v = 0
while True:
    jogador = int(input("digite um numero:"))
    computador = randint(0,10)
    total = jogador + computador
    tipo = " "
    while tipo not in "PpIi":
        tipo = str(input("escolha imparnou par [p/i]:")).upper().strip()[0]
    print(f"vc jogou {jogador} e o computador jogou {computador} e o total é {total}")
    if tipo == "P":
        if total % 2 == 0:
            print("vc venceu")
            v += 1
        else:
            print("vc perdeu")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("vc venceu")
            v += 1
        else:
            print("vc perdeu")
            break
            print("vamos jogar novamente...")
    print("goodbay....")