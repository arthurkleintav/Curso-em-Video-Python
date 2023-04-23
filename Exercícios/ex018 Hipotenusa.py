from math import hypot

# co = float(input('Comprimento do Cateto Oposto: '))
# ca = float(input('Comprimento do Cateto Adjacente: '))
# hip = (ca ** 2 + co ** 2) ** (1/2)
# print('O comprimento da Hipotenusa é {:.2f}'.format(hip))

co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
#ou: hi = math(hypot(co, ca)
print('O comprimento da Hipotenusa é {:.2f}'.format(hypot(co, ca)))
