from random import randint
itens = ("pedra","papel","tesoura")
computador = randint(0,2)
print("""opções:
[0] pedra
[1] papel
[2] tesoura""")
jogador = int(input("qual a sua escolha:"))
print("-=" *10)
print("computador jogou {}".format(itens[computador]))
print("vc jogou {}".format(itens[jogador]))
print("-=" *10)
if computador == 0:
    if jogador == 0:
        print("empate")
    elif jogador == 1:
        print("jogador vence")
    elif jogador == 2:
        print("computador vence")
    else:
        print("jogada invalida")
elif computador == 1:
    if jogador == 0:
        print("computador vence")
    elif jogador == 1:
        print("empate")
    elif jogador == 2:
        print("jogador vence")
    else:
        print("jogada invalida")
elif computador == 2:
    if jogador == 0:
        print("jogador vence")
    elif jogador == 1:
        print("computador vence")
    elif jogador == 2:
        print("empate")
    else:
         print("jogada invalida")
         