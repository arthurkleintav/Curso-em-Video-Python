from random import randint
from time import sleep
jogos = []
print('-='*15)
print(f'{"Mega-Sena":^30}')
print('-='*15)
quant = int(input('Quantos jogos você quer que eu sorteie? ')) + 1
for c in range(1, quant):
    while True:
        num = randint(1, 60)
        if len(jogos) == 0:
            jogos.append(num)
        else:
            if num not in jogos:
                jogos.append(num)
            if len(jogos) == 6:
                jogos.sort()
                break
    print(f'Jogo {c}: {jogos}')
    sleep(0.5)
    jogos.clear()
print('-='*15)
print(f'{"BOA SORTE!":^30}')