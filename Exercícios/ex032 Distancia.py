dst = int(input('Distância da viagem em Km: '))
if dst <= 200:
    preco = dst * 0.5
else:
    preco = dst * 0.45
print('O preço da passagem será de R${:.2f}'.format(preco))

# dst = int(input('Distancia da viagem em Km: '))
# preco = dst * 0.5 if dst <= 200 else dst * 0.45
# print('O preço da passagem será de R${:.2f}'.format(preco))
