from math import radians, sin,cos,tan
an = float(input("digite o valor que deseja:"))
seno = sin(radians(an))
print("o angulo de {} tem o seno de {:.2f}".format(an, seno))
cos = cos(radians(an))
print("o angulo de {} tem o cos de {:.2g}".format(an, cos))
tan = tan(radians(an))
print("o angulo de {} tem o tan de {:.2f}".format(an,tan))

