t1 = float(input('primeiro segmento:'))
t2 = float(input('segundo segmento:'))
t3 = float(input('terceiro sgmento:'))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print("os segmentos acima podem forma um triangulo ", end= "")
    if t1 == t2 and t2 == t3:
        print("EQUILATERO")
    elif t1 != t2 and t2 != t3 != t1:
        print("ESCALENO")
    else:
        print("ESÓSCELES")
else:
    print("os segmentos não podem forma um triangulo")