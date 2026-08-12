distancia = float(input("qual a distancia da viajem:"))
print("vc esta prestes a comecar uma viagem de {}km".format(distancia))
if distancia <= 200:
    preço = distancia * 0,50
else:
    preço = distancia * 0.45
print("o preço da viagem custara R${}".format(preço))
