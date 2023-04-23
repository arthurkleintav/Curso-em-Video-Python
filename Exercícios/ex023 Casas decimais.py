num = int(input('Digite um número de 0 a 9999: '))
unid = num // 1 % 10
print('Unidade: {}'.format(unid))
dez = num // 10 % 10
print('Dezena: {}'.format(dez))
cent = num // 100 % 10
print('Centena: {}'.format(cent))
mil = num // 1000 % 10
print('Milhar: {}'.format(mil))