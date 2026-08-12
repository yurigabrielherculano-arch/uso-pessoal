import math
n1 = float(input("digite um numero:"))
print("o valor digitado foi {} e sua parte inteira é {}".format(n1,math.trunc(n1)))

#ou 

from math import trunc
n1= float(input("digite um numero:"))
print("o valor digitado foi {} e sua parte inteira é {}".format(n1,trunc(n1)))


# ou

n1 = float(input("digite um numero:"))
print("o valor digitado foi {} e sua parte inteira é {}".format(n1, int(n1)))
