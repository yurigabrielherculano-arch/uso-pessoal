from random import randint
from time import sleep
computador = randint(0,5)
print("-=-"*18)
print("vou pensar em um numero de 0 a 5,tente advinhar")
print("-=-"*18)
jogador = int(input("em que numero estou pensando?"))
print("-=-"*18)
print("analisando...")
sleep(1)
print("-=-"*18)
if jogador == computador:
    print("vc ganhou")
else:
    print("vc perdeu, o numero é {}".format(computador))
    