import math
ang = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(ang))
print('O ângulo {} tem o SENO de {:.2f}'.format(ang, seno))
cosseno = math.cos(math.radians(ang))
print('O ângulo {} tem o COSSENO de {:.2f}'.format(ang, cosseno))
tangente = math.tan(math.radians(ang))
print('O ângulo {} tem a TANGENTE de {:.2f}'.format(ang, tangente))